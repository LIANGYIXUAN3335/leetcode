class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = {}
        maxlength = 0
        left,right = 0, 0
        while right < len(s):
            curset[s[right]] = curset.get(s[right],0) + 1
            if curset[s[right]] > 1:
                while s[left] != s[right]:
                    curset[s[left]] = 0
                    left += 1
                left += 1
                curset[s[right]] = 1
            right += 1
            maxlength = max(maxlength, right - left)
        return maxlength
                