class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1

        return result
