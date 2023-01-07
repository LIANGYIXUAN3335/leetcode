class Solution:
    def numDecodings(self, s: str) -> int:
        # s : 12  1 2 A B
        #         12 L
        # ****** K ****
        # before k is "1"  "1,k"  "1k"   k-2 + k -1  - >k
        #             k == 0: "1,k"  不成立  k-2 -> k

        # before k is "2"  k in [0-6] "2k"  "2,k" k-2 + k -1  - >k
        #                  k > 6   "2k" 不成立  "2,K"   K - 1 - > K
        #                  k == 0: "2,k"  不成立  k-2 -> k
        # before k is "0" or "3--9"    "nK" 不成立  k -1 ->k
        #                 k == 0 return 0 
        #                 k != 0  k -1 -> k
        if len(s) == 0:
            return 0
        if s[0] == "0" :
            return 0
        first ,second = 1,1
        for i in range(1, len(s)):
            if s[i - 1] == "1":
                if s[i] == "0":
                    first, second = second , first
                else :
                    temp = first + second
                    first = second
                    second = temp
            elif s[i - 1] == "2":
                if s[i] == "0":
                    first, second = second , first
                elif s[i] in "123456" :
                    temp = first + second
                    first = second
                    second = temp
                else:
                    first = second
            else:
                if s[i] == "0":
                    return 0
                else:
                    first = second
        return second