class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        c = 0
        for ch in t:
            if ch == s[c]:
                c += 1
            if c == len(s):
                return True
        return False
