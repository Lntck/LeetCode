class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k: int):
            res = 0
            for i in piles:
                res += (i + k - 1) // k
            return res

        mx = max(piles)
        l, r = 1, mx
        while l <= r:   
            mid = (l + r) // 2
            k = check(mid)

            if k > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
