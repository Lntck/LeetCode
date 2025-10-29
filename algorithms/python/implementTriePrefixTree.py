from collections import defaultdict


class Trie:
    def __init__(self, is_key: bool = False):
        self.is_key = is_key
        self.leaves = defaultdict(Trie)

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.leaves[ch]
        node.is_key = True
    
    def _find_leaf(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            if ch not in node.leaves:
                return None
            node = node.leaves[ch]
        return node

    def search(self, word: str) -> bool:
        leaf = self._find_leaf(word)
        return leaf.is_key if leaf else False

    def startsWith(self, prefix: str) -> bool:
        return self._find_leaf(prefix) is not None
