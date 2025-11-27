class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float("inf")] * (amount)
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1
