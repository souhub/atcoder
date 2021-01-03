// Best Time to Buy and Sell Stock

package main

func maxProfit(prices []int) int {
	profit := 0
	for i := 0; i < len(prices)-1; i++ {
		for j := i + 1; j < len(prices); j++ {
			if profit < prices[j]-prices[i] {
				profit = prices[j] - prices[i]
			}
		}
	}
	return profit
}
