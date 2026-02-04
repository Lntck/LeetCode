class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []
        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l]**2)
                l += 1
            else:
                result.append(nums[r]**2)
                r -= 1
        return result[::-1]
        