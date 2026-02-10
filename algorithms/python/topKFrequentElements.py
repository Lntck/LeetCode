# import heapq


class Solution:
    # time: O(n logk), space: O(n)
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     frequency = {}
    #     for n in nums:
    #         frequency[n] = frequency.get(n, 0) + 1

    #     heap = []
    #     for key, freq in frequency.items():
    #         heapq.heappush(heap, (freq, key))
    #         if len(heap) > k:
    #             heapq.heappop(heap)
    #     return [n for _, n in heap]

    # time: O(n), space: O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        buckets = [[] for _ in range(len(nums)+1)]

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        res = [] 
        for i in range(len(buckets) - 1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
