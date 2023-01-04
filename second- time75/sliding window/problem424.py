class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slidewindow = {}
        left = 0
        curmax = 0
        maxlength = 0
        for right in range(len(s)):
# for is more efficient than while
            slidewindow[s[right]] = slidewindow.get(s[right] , 0) + 1
            if right - left + 1 - max(slidewindow.values()) <= k:
                maxlength = max(maxlength,right - left + 1 )
            else:
                slidewindow[s[left]] = slidewindow[s[left]] - 1
                left += 1
        return maxlength