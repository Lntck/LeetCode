class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current: list[int], i: int):
            if i == len(nums):
                result.append(current[:])
                return
            for j in range(i, len(nums)):
                current[i], current[j] = current[j], current[i]
                backtrack(current, i+1)
                current[i], current[j] = current[j], current[i]
        backtrack(nums, 0)
        return result
