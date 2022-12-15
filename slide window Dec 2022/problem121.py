class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            else:
                profit = max(i-minPrice,profit) 
        return profit