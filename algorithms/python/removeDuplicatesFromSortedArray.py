class Solution:
    # Key idea is to sort Not to remove
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[k] = nums[i]
                prev = nums[i]
                k += 1
        return k
