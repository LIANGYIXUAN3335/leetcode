class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            #odd length
            left, right = i,i
            length = 1
            while left >=0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            #even length
            if i < len(s) - 1:
                left,right = i,i+1
                while left >=0 and right < len(s) and s[left] == s[right]:
                    res += 1
                    left -=  1
                    right += 1
        return res