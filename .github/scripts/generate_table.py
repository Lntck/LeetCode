import os
import requests
import logging
import re


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

LANG_DIRS = {
    "cpp": "C++",
    "python": "Python",
    "java": "Java",
}

LANG_EXTENSIONS = (".cpp", ".py", ".java")

INT_TO_DIFFICULTY = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}


def fetch_question(slug):
    url = f"https://leetcode.com/api/problems/all/?search={slug}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for question in data.get("stat_status_pairs", []):
            if question["stat"]["question__title_slug"] == slug:
                return {
                    "question_id": question["stat"]["question_id"],
                    "title": question["stat"]["question__title"],
                    "difficulty": INT_TO_DIFFICULTY[question["difficulty"]["level"]],
                }
    except requests.RequestException as e:
        logging.error(f"Error fetching data for slug '{slug}': {e}")
    return None


def extract_slug(filename):
    # "twoSum.cpp" -> "two-sum"
    # "jumpGameII.py" -> "jump-game-ii"
    # "insertDeleteGetrandomO1.cpp" -> "insert-delete-getrandom-o1"
    filename = filename.rsplit('.', 1)[0]
    parts = re.findall(
        r'[A-Z]{2,}(?=[A-Z][a-z]|[0-9]|$)'
        r'|[A-Z]?[a-z]+'
        r'|[A-Z][0-9]+'
        r'|[0-9]+',
        filename
    )
    slug = '-'.join(part.lower() for part in parts)
    return slug


def get_solutions():
    solutions = []
    for lang_folder, lang_name in LANG_DIRS.items():
        folder = f"./algorithms/{lang_folder}"
        if not os.path.exists(folder):
            logging.warning(f"Folder not found: {folder}")
            continue
        
        for file in os.listdir(folder):
            if file.endswith(LANG_EXTENSIONS):
                slug = extract_slug(file)
                question = fetch_question(slug)
                if not question:
                    logging.warning(f"Question not found for slug: {slug}")
                    continue
                question_id = question.get("question_id")
                title = question.get("title")
                difficulty = question.get("difficulty")
                solution_link = f"[{lang_name}](./algorithms/{lang_folder}/{file})"
                solutions.append((int(question_id), title, slug, solution_link, difficulty))
                logging.info(f"Found: #{question_id} {title} [{difficulty}]")
    return sorted(solutions, key=lambda x: x[0])


def generate_table():
    rows = get_solutions()
    if not rows:
        logging.warning("No solutions found.")

    table = "| # | Title | Solution | Difficulty |\n|---|-------|----------|------------|\n"
    for id, title, slug, solution_link, difficulty in rows:
        title_link = f"[{title}](https://leetcode.com/problems/{slug}/)"
        table += f"|{id}|{title_link}|{solution_link}|{difficulty}|\n"
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

        new_table = "## Solutions Table\n\n" + generate_table() + "\n"
        updated_content = content[:start] + new_table + content[end:]

        with open("README.md", "w", encoding="utf-8") as file:
            file.write(updated_content)
        logging.info("README.md updated successfully.")
    except Exception as e:
        logging.error(f"Failed to update README.md: {e}")


if __name__ == "__main__":
    main()