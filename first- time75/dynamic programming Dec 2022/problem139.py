# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         wordDict.sort(key = lambda x : len(x),reverse =  True)
#         dp = [0] * (len(s) + 1)
#         def dfs(s,index):
#             if len(s) == index:
#                 return True
#             for i in wordDict:
#                 if s[index :].startswith(i):
#                     if dp[index + len(i)] != 0:
#                         if dp[index + len(i)]:
#                             return True
#                     else:
#                         if dfs(s,index + len(i)):
#                             dp[index + len(i)] = True
#                             return True
#                         else:
#                             dp[index + len(i)] = False       
#             return False
#         return dfs(s,0)


# for the problem which from begin to end have multiple ways 
# from back to start will be the better solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1,-1):
            for j in wordDict:
                if s[i:].startswith(j):
                    dp[i] = dp[i + len(j)]
                if dp[i]:
                    break
        return dp[0]