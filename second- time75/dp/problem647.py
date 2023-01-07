class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        def oddhelper(s: str,index : int):
            nonlocal ans
            left = right = index 
            while left >= 0 and right < len(s):
                if s[left] == s[right] :
                    ans += 1
                else:
                    break
                left -= 1
                right +=1

        def evenhelper( s: str,left : int,right :int) -> str:
            nonlocal ans
            while left >= 0 and right < len(s):
                if s[left] == s[right] :
                    ans += 1
                else:
                    break
                left -= 1
                right +=1
        for i in range(0, len(s)):
            oddhelper(s,i)
        for i in range(0, len(s) - 1):
            evenhelper(s,i,i+1)
        return ans