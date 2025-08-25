class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

        result = ""

        i = len(nums) - 1
        while num:
            div = num // nums[i]
            while div:
                result += symbols[i]
                div -= 1
            num %= nums[i]
            i -= 1

        return result
