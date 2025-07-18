class Solution:
    # Foes not use any built-in functions such as split(), join(), reversed(), or slicing (e.g., [::-1]).
    # It processes the string manually and uses only constant extra space (excluding the output string).
    # def reverseWords(self, s: str) -> str:
    #     result = ""
    #     word = ""
    #     for i in range(len(s)):
    #         if s[i] != " ":
    #             word += s[i]
    #         elif s[i] == " " and word:
    #             result = ((word + " " + result) if result else word)
    #             word = ""

    #     if word:    
    #         return ((word + " " + result) if result else word)
    #     return result
    

    # if built-in functions are allowed, the solution can be simplified:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])