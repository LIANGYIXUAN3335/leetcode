class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            for j in wordDict:
                if dp[i] ==  True:
                    break
                if s[i :].startswith(j):
                    dp[i] = dp[i + len(j)]
        return dp[0]
