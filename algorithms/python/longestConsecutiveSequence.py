class Solution:
    # O(n) - time complexity, O(n) - space complexity
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for n in unique:
            if n-1 not in unique:
                c = 1
                while n + c in unique:
                    c += 1
                longest = max(c, longest)
        return longest
