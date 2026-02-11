class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_decreasing, is_increasing = True, True

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                is_decreasing = False
            if nums[i] < nums[i-1]:
                is_increasing = False
            if not is_increasing and not is_decreasing:
                return False
        return is_increasing or is_decreasing
        