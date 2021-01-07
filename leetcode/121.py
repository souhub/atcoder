# Best Time to Buy and Sell Stock

# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if profit < prices[j]-prices[i]:
                    profit = prices[j]-prices[i]
        return profit


# Passed
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i]-min_price)

        return profit
