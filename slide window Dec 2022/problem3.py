class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentset = set()
        i = j = 0
        maxslidewindow = 0
        if len(s) == 1:
            return 1
        while j <  len(s):
            if s[j] in currentset:
                currentset.remove(s[i])
                i += 1
            else:
                currentset.add(s[j])
                j += 1
                maxslidewindow = max(j - i , maxslidewindow)
        return maxslidewindow