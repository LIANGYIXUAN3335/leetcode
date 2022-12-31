class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        ans =[1]*m
        for i in range(1,n):
            for j in range(1,m):
                ans[j] = ans[j] + ans[j-1]
        return ans[-1]
