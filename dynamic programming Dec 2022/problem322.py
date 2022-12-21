class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [float("inf")] * (amount + 1)
        res[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                res[i] = 1
                continue
            minvalue = float("inf")
            for j in coins:
                if i > j:
                    minvalue = min(minvalue,res[i-j] +1)
            res[i] = minvalue 
        if res[-1] == float("inf"):
            return -1
        else:
            return res[-1]
