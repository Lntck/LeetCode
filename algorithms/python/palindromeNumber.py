class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        orig = x
        rever = 0
        while orig:
            rever = rever * 10 + orig % 10
            orig //= 10

        return x == rever