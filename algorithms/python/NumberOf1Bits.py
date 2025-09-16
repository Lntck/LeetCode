class Solution:
    # Pythonic approach
    # def hammingWeight(self, n: int) -> int:
    #     return bin(n).count("1")

    # Bit checking
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n:
    #         count += n & 1
    #         n >>= 1
    #     return count

    # Optimized Approach: Kernighan's algorithm
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count
