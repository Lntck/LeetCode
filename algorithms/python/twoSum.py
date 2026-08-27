class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct = dict()
        for index, n in enumerate(nums):
            if n in dct:
                return [dct[n], index]
            dct[target - n] = index
        return []
