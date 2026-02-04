class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxlen = 0
        count_zero = 0
        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                count_zero += 1
            
            while count_zero > 1:
                if nums[l] == 0:
                    count_zero -= 1
                l += 1
            maxlen = max(maxlen, r-l)
        return maxlen

