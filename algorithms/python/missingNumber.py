class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = len(nums) * (len(nums) + 1) // 2
        for n in nums:
            total -= n
        return int(total)
        