class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        number = 0
        for n in nums:
            if number ^ (1 << n) < number:
                return n
            else:
                number ^= (1 << n)
        return -1
