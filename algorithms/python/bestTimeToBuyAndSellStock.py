class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        zakup = prices[0]
        sell = 0
        for i in range(len(prices)):
            if zakup > prices[i]:
                zakup = prices[i]
            elif sell < prices[i] - zakup:
                sell = prices[i] - zakup
        return sell
