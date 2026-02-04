class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        ptr = 0
        while ptr < len(nums):
            start = ptr
            while ptr + 1 < len(nums) and nums[ptr] + 1 == nums[ptr+1]:
                ptr += 1
            result.append(f"{nums[start]}" if start == ptr else f"{nums[start]}->{nums[ptr]}")
            ptr += 1
        return result