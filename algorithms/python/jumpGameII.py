class Solution:
    # Initial approach: Greedy algorithm that selects the next jump by checking all possible positions
    # within the current jump range and choosing the one that allows the farthest reach.
    # def jump(self, nums: List[int]) -> int:
    #     cost = 0
    #     i = 0
    #     while i < len(nums) - 1:
    #         maxJump = 0
    #         index = 0
    #         j = 1
    #         while i+j < len(nums) and j <= nums[i]:
    #             if maxJump < nums[i+j] + i + j:
    #                 maxJump = nums[i+j] + i + j
    #                 index = i+j
    #             j += 1
    #         if i+j == len(nums):
    #             return cost + 1
    #         cost += 1
    #         i = index
    #     return cost

    # Optimized approach: Optimized greedy algorithm that tracks the current jump boundary (`end`) and 
    # the farthest reachable position (`farther`). Minimizes jumps by expanding the boundary only when necessary.
    def jump(self, nums: List[int]) -> int:
        cost = 0
        end = 0
        farther = 0

        for i in range(len(nums) - 1):
            farther = max(farther, nums[i] + i)
            if farther >= len(nums) - 1:
                return cost + 1
            if i == end:
                cost += 1
                end = farther
        return cost
