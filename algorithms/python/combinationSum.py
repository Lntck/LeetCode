class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(current, i):
            if sum(current) > target: return
            if sum(current) == target:
                result.append(current[:])
                return
            for j in range(i, len(candidates)):
                backtrack(current + [candidates[j]], j)
        backtrack([], 0)
        return result
