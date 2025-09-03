class Solution:
    # Different approach:
    # def reverseBits(self, n: int) -> int:
    #     return int(f'{n:032b}'[::-1], base=2)

    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result
