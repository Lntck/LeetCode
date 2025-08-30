class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums

        result = []
        start = 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i+1] - 1:
                if start == i:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i]}")
                start = i + 1
        return result
