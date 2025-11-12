class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        minim = float("-inf")
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            l_neighbor = nums[mid-1] if mid > 0 else minim
            r_neighbor = nums[mid+1] if mid < len(nums)-1 else minim
            if nums[mid] > l_neighbor and nums[mid] > r_neighbor:
                return mid
            elif l_neighbor > r_neighbor:
                right = mid - 1
            else:
                left = mid + 1
        return left