class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(current: list[int], k: int) -> None:
            if k == 0:
                result.append(current)
                return
            for i in range(current[-1]+1, n+1):
                backtrack(current + [i], k-1)
        
        for i in range(1, n+1):
            backtrack([i], k-1)
        return result
