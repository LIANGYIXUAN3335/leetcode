class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        else:
            ans = s[0]
            length = 1
        def oddhelper(s: str,index : int):
            nonlocal ans, length
            left ,right = index - 1,index + 1
            curlength = 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curlength += 2
                    if curlength > length :
                        length = curlength
                        ans = s[left:right+1]
                else:
                    break
                left -= 1
                right +=1
            if curlength > length :
                length = curlength
                ans = s[left:right+1]

        def evenhelper( s: str,left : int,right :int) -> str:
            nonlocal ans, length
            curlength = 0
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    curlength += 2
                    if curlength > length :
                        length = curlength
                        ans = s[left:right+1]
                else:
                    break
                left -= 1
                right +=1
        for i in range(0, len(s)):
            oddhelper(s,i)
        for i in range(0, len(s) - 1):
            evenhelper(s,i,i+1)
        return ans