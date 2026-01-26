class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            max_sum = max(max_sum + nums[i], nums[i])
            result = max(result, max_sum)
        return result
