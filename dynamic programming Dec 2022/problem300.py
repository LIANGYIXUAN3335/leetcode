class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlength = [1] * len(nums)
        for i in range(len(nums)):
            curmax = 1
            for j in range(i-1,-1,-1):            
                if nums[i] > nums[j]:
                    curmax = max(curmax,maxlength[j]+1)
                    maxlength[i] = curmax
        return max(maxlength)