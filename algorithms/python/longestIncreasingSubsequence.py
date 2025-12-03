class Solution:
    # Naive approach O(n^2)
    # def lengthOfLIS(self, nums: list[int]) -> int:
    #     dp = [1] * len(nums)

    #     for i in range(1, len(nums)):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[j] + 1, dp[i])
    #     return max(dp)

    # Optimized approach O(n log n)
    def lengthOfLIS(self, nums: list[int]) -> int:
        result = nums[:1]

        for i in range(1, len(nums)):
            if nums[i] <= result[-1]:
                left = 0
                right = len(result) - 1
                while left < right:
                    mid = (left + right) // 2
                    if result[mid] < nums[i]:
                        left = mid + 1
                    else:   
                        right = mid
                result[left] = nums[i]
            else:
                result.append(nums[i])
        return len(result)