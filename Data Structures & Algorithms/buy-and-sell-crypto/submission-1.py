class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSell = max(prices)
        maxP = 0

        for sell in prices:
            maxP = max(maxP, sell-minSell)
            minSell = min(minSell, sell)
        return maxP