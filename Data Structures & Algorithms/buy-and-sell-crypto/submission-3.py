class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            profit = price-min_buy
            max_profit = max(max_profit, profit)
            min_buy = min(min_buy, price)
        return max_profit
