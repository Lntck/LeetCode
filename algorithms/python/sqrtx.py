class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        left, right = 0, x // 2
        while left <= right:
            mid = (right + left) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid
        return right
