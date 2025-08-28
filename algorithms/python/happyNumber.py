class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n != 1 and n not in history:
            history.add(n)
            n = sum(map(lambda x: int(x)**2, str(n)))
        return n == 1
