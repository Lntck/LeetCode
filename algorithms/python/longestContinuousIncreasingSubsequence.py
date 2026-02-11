class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        longest = 1
        start = 0
        for end in range(1, len(nums)):
            if nums[end-1] >= nums[end]:
                longest = max(longest, end - start)
                start = end
        return max(longest, len(nums) - start)