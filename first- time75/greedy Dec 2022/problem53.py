class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total, minpre,maxsubvalue = 0, 0,nums[0]
        for i in nums:
            total += i
            maxsubvalue = max(maxsubvalue,total - minpre)
            minpre = min(minpre,total)
        return maxsubvalue