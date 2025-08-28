class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == len(set(nums)):
            return False
        
        nearDuplicate = {}
        for i, n in enumerate(nums):
            if n in nearDuplicate:
                if i - nearDuplicate[n] <= k:
                    return True
            nearDuplicate[n] = i
        return False
