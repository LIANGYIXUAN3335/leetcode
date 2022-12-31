class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n != 0:
            n &= n -1 
            total += 1
        return total