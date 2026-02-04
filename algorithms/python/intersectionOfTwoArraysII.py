from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            small, big = nums1, nums2
        else:
            small, big = nums2, nums1

        result = []
        freq_nums = Counter(small)

        for n in big:
            if freq_nums[n] > 0:
                freq_nums[n] -= 1
                result.append(n)
        return result
