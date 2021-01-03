# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if profit < prices[j]-prices[i]:
                    profit = prices[j]-prices[i]
        return profit
