class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf")
        maxposi, minnega = 1,1
        for i in nums:
            temp = max(maxposi * i, minnega * i, i)
            minnega = min(maxposi * i, minnega * i, i)
            maxposi = temp
            res = max(maxposi,res)
        return res