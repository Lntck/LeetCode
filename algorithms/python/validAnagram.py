class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {ch: s.count(ch) for ch in set(s)} == {ch: t.count(ch) for ch in set(t)}
