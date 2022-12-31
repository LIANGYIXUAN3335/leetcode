class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 2
        for i in range(2,n):
            temp = first + second
            first = second
            second = temp
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return temp