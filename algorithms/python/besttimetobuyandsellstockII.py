class Solution:
    # Initial approach: Track buy price and max sell, but logic was more complex
    # def maxProfit(self, prices: List[int]) -> int:
    #     zakup = float("+inf")
    #     max_sell = 0
    #     profit = 0
    #     for i in range(len(prices)):
    #         if zakup > prices[i] or prices[i] < prices[i-1]:
    #             zakup = prices[i]
    #             profit += max_sell
    #             max_sell = 0
    #         else:
    #             if prices[i] - zakup > max_sell:
    #                 max_sell = prices[i] - zakup
    #     return profit + max_sell

    # Optimized approach: sell immediately when find a larger price
    def maxProfit(prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
