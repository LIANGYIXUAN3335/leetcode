class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        premin,maxres = float("inf"),0
        for i in prices:
            maxres = max(i-premin,maxres)
            premin = min(premin,i)
        return maxres
        