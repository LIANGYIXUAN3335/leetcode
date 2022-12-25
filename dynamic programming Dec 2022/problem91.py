class Solution:
    def numDecodings(self, s: str) -> int:
        sum1 = 1
        sum2 = 1
        if not s or s[0] == "0":
            return 0
        cur = 1
        for i in range(1 , len(s)):
            if s[i - 1] == "1":
                if s[i] == "0":
                    cur = sum1
                else:
                    cur = sum1 + sum2
            elif s[i - 1] == "2":
                if s[i] == "0":
                    cur = sum1
                elif ord(s[i]) - ord("0") <= 6 :
                    cur = sum1 + sum2
                else :
                    cur =  sum2
            else:
                if s[i] == "0":
                    return 0
                else:
                    cur =  sum2
            sum1 = sum2
            sum2 = cur
        return cur