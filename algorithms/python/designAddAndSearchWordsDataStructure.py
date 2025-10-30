from collections import defaultdict


class WordDictionary:
    def __init__(self, is_key: bool = False):
        self.is_key = is_key
        self.leaves = defaultdict(WordDictionary)

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.leaves[ch]
        node.is_key = True

    def search(self, word: str) -> bool:
        node = self
        for i in range(len(word)):
            if word[i] == ".":
                for leaf in node.leaves:
                    if node.leaves[leaf].search(word[i+1:]):
                        return True
                return False
            elif word[i] not in node.leaves:
                return False
            else:
                node = node.leaves[word[i]]
        return node.is_key
