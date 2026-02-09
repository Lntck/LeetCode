class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum, result = 0, 0
        hashmap = {0: 1}

        for n in nums:
            prefix_sum += n
            result += hashmap.get(prefix_sum - k, 0)
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
        return result