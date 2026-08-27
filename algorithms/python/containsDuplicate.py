class Solution:
    # O(n) time complexity, O(n) space complexity
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     used = set()
    #     for n in nums:
    #         if n in used:
    #             return True
    #         used.add(n)
    #     return False

    # O(n) time complexity, O(n) space complexity, cuz of C running faster
    def containsDuplicate2(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
