class Solution:
    # Initial approach:
    # Checks if you can reach the last index starting from the first, 
    # where each element represents your max jump length at that position
    # Too complex
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     path = [False] * n
    #     path[0] = True
    #     for i in range(n):
    #         if path[i]:
    #             max_jump = n if (i + nums[i]) >= n else i + nums[i] + 1
    #             path[i:max_jump] = ((max_jump - i)) * [True]
    #     return path[-1]
    # Optimized approach: Tracks maximum reachable distance at each step.
    def canJump(nums: list[int]) -> bool:
        jump = nums[0]
        for n in nums:
            if jump < 0:
                return False
            elif n > jump:
                jump = n
            jump -= 1
        return True
