class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = rest = 0
        for price in prices[1:]:
            p_hold = hold
            p_sold = sold
            p_rest = rest
            hold = max(p_hold, p_rest-price)
            sold = p_hold+price
            rest = max(p_rest, p_sold)
        return max(sold, rest)