class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 1e4+1

        for price in prices:
            max_profit = max(price-min_price, max_profit)
            min_price = min(min_price, price)
        return max_profit