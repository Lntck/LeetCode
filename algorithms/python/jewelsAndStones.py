class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewellery = set(jewels)
        return sum(1 for stone in stones if stone in jewellery)
