class Solution:
    # Two Pointer Solution, time complexity - O(n)
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mx_area = 0

        while l < r:
            mx_area = max((r-l)*min(height[l], height[r]), mx_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mx_area
