class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        result_max = result_min = nums[0]
        max_sum = min_sum = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            max_sum = max(max_sum + nums[i], nums[i])
            min_sum = min(min_sum + nums[i], nums[i])
            result_max = max(result_max, max_sum)
            result_min = min(result_min, min_sum)
        return result_max if result_max < 0 else max(total - result_min, result_max)
