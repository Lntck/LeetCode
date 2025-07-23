class Solution:
    # time - O(n), space - O(n)
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)

    #     mx = 0
    #     left_max = [0] * n
    #     for i in range(n):
    #         left_max[i] = mx
    #         mx = max(mx, height[i])
        
    #     mx = 0
    #     right_max = [0] * n
    #     for i in range(n-1, -1, -1):
    #         right_max[i] = mx
    #         mx = max(mx, height[i])

    #     c = 0
    #     for i in range(n):
    #         c += max(0, min(left_max[i], right_max[i]) - height[i])
    #     return c
    #
    # time - O(n), space - O(1)
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                water += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
                l += 1
            else:
                water += max(0, max_r - height[r])
                max_r = max(max_r, height[r])
                r -= 1
        return water