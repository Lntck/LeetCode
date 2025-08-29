import logging
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import requests


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@dataclass(frozen=True, order=True)
class ProblemInfo:
    """Represents metadata for a LeetCode problem."""
    question_id: int
    title: str
    difficulty: str


@dataclass(frozen=True, order=True)
class SolutionInfo:
    """Represents a solution to a LeetCode problem in a specific language."""
    question_id: int
    title: str
    slug: str
    solution_link: str
    difficulty: str

    @property
    def problem_link(self) -> str:
        """
        Generate a Markdown-formatted link to the problem on LeetCode.

        Returns:
            str: Markdown link with problem title pointing to LeetCode.
        """
        return f"[{self.title}](https://leetcode.com/problems/{self.slug}/)"


class LeetCodeManager:
    """
    Manages fetching LeetCode problems and generating a solutions table.
    
    Attributes:
        base_folder (str): Base folder where solution files are stored.
        LANG_DIRS (dict): Mapping of folder names to language display names.
        LANG_EXTENSIONS (tuple): Allowed file extensions for solutions.
        questions (dict): Cached mapping from problem slug to ProblemInfo.
    """

    INT_TO_DIFFICULTY = {
        1: "🟢 Easy",
        2: "🟡 Medium",
        3: "🔴 Hard",
    }

    def __init__(self, base_folder: str = "./algorithms", LANG_DIRS: Dict[str, str] | None = None, LANG_EXTENSIONS: Tuple[str, ...] | None = None):
        """
        Initialize LeetCodeManager, fetches all problem data from LeetCode.

        Args:
            base_folder (str, optional): Base folder containing solution files.
            LANG_DIRS (dict, optional): Folder -> language display name mapping.
            LANG_EXTENSIONS (tuple, optional): Allowed file extensions.
        """
        self.base_folder = base_folder
        self.base_url = "https://leetcode.com/api/problems/all/"
        self.LANG_DIRS = LANG_DIRS if LANG_DIRS else {"cpp": "C++", "python": "Python", "java": "Java"}
        self.LANG_EXTENSIONS = LANG_EXTENSIONS if LANG_EXTENSIONS else (".cpp", ".py", ".java")
        self.questions = self.fetch_questions()
    
    def fetch_questions(self, max_retries: int = 3, timeout: int = 10, backoff: float = 2) -> dict[str, ProblemInfo]:
        """
        Fetch all LeetCode problems from the API with retry/backoff.

        Args:
            max_retries (int): Maximum number of retries on network failure.
            timeout (int): Request timeout in seconds.
            backoff (float): Initial backoff time between retries, doubles each attempt.

        Returns:
            dict[str, ProblemInfo]: Mapping of problem slug to ProblemInfo.

        Raises:
            RuntimeError: If unable to fetch any problems after all retries.
        """
        questions: dict[str, ProblemInfo] = {}
        for attempt in range(1, max_retries+1):
            try:
                response = requests.get(self.base_url, timeout=timeout)
                response.raise_for_status()
                data = response.json()
                for question in data.get("stat_status_pairs", []):
                    slug = question["stat"]["question__title_slug"]
                    questions[slug] = ProblemInfo(
                        question_id=int(question["stat"]["question_id"]),
                        title=question["stat"]["question__title"],
                        difficulty=self.INT_TO_DIFFICULTY[question["difficulty"]["level"]],
                    )
                logging.info(f"Fetched {len(questions)} questions successfully on attempt {attempt}.")
                return questions
            except requests.Timeout:
                logging.warning(f"Timeout on attempt {attempt}/{max_retries}. Retrying in {backoff} sec...")
            except requests.RequestException as e:
                logging.error(f"Network error on attempt {attempt}/{max_retries}: {e}")
            
            if attempt < max_retries:
                time.sleep(backoff)
                backoff *= 2
        
        logging.error("No questions fetched. Stopping execution.")
        raise RuntimeError("Cannot continue without LeetCode questions.")

    @staticmethod
    def extract_slug(filename: Path) -> str:
        """
        Convert a solution filename to a LeetCode problem slug.

        Example:
            "twoSum.cpp" -> "two-sum"
            "jumpGameII.py" -> "jump-game-ii"
            "insertDeleteGetrandomO1.cpp" -> "insert-delete-getrandom-o1"
            "reverseWordsInAString.py" -> "reverse-words-in-a-string"

        Args:
            filename (Path): Path object representing the solution file.

        Returns:
            str: Problem slug suitable for API lookup or links.
        """
        filename = filename.stem

        parts = re.findall(
            r'[A-Z][0-9]+|'
            r'[A-Z]+(?=[A-Z][a-z])|'
            r'[0-9]*[A-Z]?[a-z]+|'
            r'[A-Z]+|' 
            r'[0-9]+',
            filename
        )

        slug = '-'.join(part.lower() for part in parts)
        return slug

    def get_solutions(self) -> List[SolutionInfo]:
        """
        Scan the local solution folders and match files to fetched LeetCode problems.

        Returns:
            List[SolutionInfo]: Sorted list of SolutionInfo objects for all found solutions.
        """
        solutions: List[SolutionInfo] = []
        for lang_folder, lang_name in self.LANG_DIRS.items():
            folder_path = Path(self.base_folder) / lang_folder
            if not folder_path.exists():
                logging.warning(f"Folder not found: {folder_path}")
                continue
            
            for file_path in folder_path.iterdir():
                if file_path.suffix.lower() in self.LANG_EXTENSIONS:
                    slug = self.extract_slug(file_path)
                    question = self.questions.get(slug)
                    if not question:
                        logging.warning(f"Question not found for slug: {slug}")
                        continue

                    solutions.append(
                        SolutionInfo(
                            question_id=question.question_id,
                            title=question.title,
                            slug=slug,
                            solution_link=f"[{lang_name}]({file_path.as_posix()})",
                            difficulty=question.difficulty,
                            )
                        )
                    logging.info(f"Found: #{question.question_id} {question.title} [{question.difficulty}]")
        return sorted(solutions)

    def generate_table(self) -> str:
        """
        Generate a Markdown table for README with all solutions.

        Returns:
            str: Markdown formatted table containing all solutions.
        """
        solutions = self.get_solutions()
        if not solutions:
            logging.warning("No solutions found.")

        table = "| # | Title | Solution | Difficulty |\n|---|-------|----------|------------|\n"
        for solution in solutions:
            table += f"|{solution.question_id}|{solution.problem_link}|{solution.solution_link}|{solution.difficulty}|\n"
        return table


def main():
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()

        start = content.find("## Solutions Table")
        end = content.find("## Structure")

        if start == -1 or end == -1:
            logging.error("Table section not found in README.md")
            return
        
        manager = LeetCodeManager()
        updated_content = f"{content[:start]}## Solutions Table\n\n{manager.generate_table()}\n{content[end:]}"

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)

        logging.info("README.md updated successfully.")
    except Exception as e:
        logging.error(f"Failed to update README.md: {e}")


if __name__ == "__main__":
    main()