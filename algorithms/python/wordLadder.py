class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord: return 1

        choices = set("".join(wordList))
        queue = deque([(beginWord, 1)])
        wordList = set(wordList)
        visited = {beginWord}
        while queue:
            word, transformations = queue.popleft()
            if word == endWord:
                return transformations

            for i in range(len(word)):
                for step in choices:
                    new_word = word[:i] + step + word[i+1:]
                    if new_word in wordList and new_word not in visited:
                            visited.add(new_word)
                            queue.append((new_word, transformations + 1))
        return 0
