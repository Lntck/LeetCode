class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     s = "".join([ch for ch in s.lower() if ch.isalnum()])
    #     return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True