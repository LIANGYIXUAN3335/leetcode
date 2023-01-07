class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob0, rob1= 0,0
        for i in range(len(nums)):
            temp =  max(rob0 + nums[i] ,rob1)
            rob0 = rob1
            rob1 = temp
        return max(rob0, rob1)