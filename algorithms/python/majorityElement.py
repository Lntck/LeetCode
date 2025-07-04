class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        maj = nums[0]
        for i in range(len(nums)):
            if c == 0:
                maj = nums[i]
                c = 1
            elif nums[i] == maj:
                c += 1
            else:
                c -= 1
        return maj
