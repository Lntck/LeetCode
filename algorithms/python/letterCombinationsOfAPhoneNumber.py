class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_to_letter = {
            "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []
        def backtrack(i, current):
            if len(current) == len(digits):
                result.append(current)
                return
            
            for ch in digit_to_letter[digits[i]]:
                backtrack(i+1, current + ch)
            return
        
        backtrack(0, "")
        return result
