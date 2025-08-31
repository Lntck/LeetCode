class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        n = len(nums)
        min_len = n
        l, window_sum = 0, 0

        for r in range(n):
            window_sum += nums[r]

            while window_sum >= target:
                min_len = min(min_len, r-l+1)
                window_sum -= nums[l]
                l += 1
        return min_len
