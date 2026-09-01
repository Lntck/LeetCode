class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        mx_area = 0
        for i in range(len(heights)+1):
            h = 0 if i == len(heights) else heights[i]
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                mx_area = max(mx_area, width * height)
            stack.append(i)
        return mx_area
