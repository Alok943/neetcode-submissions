class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        buymin = prices[i]
        profit = 0
        for i in range(len(prices)):
            buymin = min(prices[i],buymin)
            if buymin < prices[i]:
                profit = max(profit,(prices[i] - buymin))
        return profit