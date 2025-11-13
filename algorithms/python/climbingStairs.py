class Solution:
    # Classic aprroach
    # def climbStairs(self, n: int) -> int:
    #     ways = [1] * (n + 1)
    #     for i in range(2, n+1):
    #         ways[i] = ways[i-2] + ways[i-1]
    #     return ways[-1]

    # Optimized to O(1) space complexity
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b
