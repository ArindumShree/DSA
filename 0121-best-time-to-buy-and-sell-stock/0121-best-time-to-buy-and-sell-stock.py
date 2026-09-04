class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=prices[0]
        for i in prices:
            min_price=min(min_price,i)
            profit=i-min_price
            max_profit=max(profit,max_profit)
        return max_profit