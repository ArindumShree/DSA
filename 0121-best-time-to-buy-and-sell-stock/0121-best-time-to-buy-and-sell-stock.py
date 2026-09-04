class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in prices:
            profit=i-min_price
            max_profit=max(profit,max_profit)
            min_price=min(min_price,i)
        return max_profit