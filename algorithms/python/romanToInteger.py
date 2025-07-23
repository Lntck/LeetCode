class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000,
        }

        res = 0
        prev = 0
        for i in range(len(s)-1, -1, -1):
            curr = rom_to_int[s[i]]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res
