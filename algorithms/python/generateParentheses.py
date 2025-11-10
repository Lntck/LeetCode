class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current: str, count_open: int) -> None:
            if len(current) == 2 * n:
                if count_open == 0:
                    result.append(current)
                return
            if count_open < n:
                backtrack(current + "(", count_open+1)
            if count_open > 0:
                backtrack(current + ")", count_open-1)

        backtrack("", 0)
        return result
