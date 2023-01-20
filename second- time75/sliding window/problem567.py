class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window --s1
        # right point -> sliding window [0]* 26
        # left point -> sliding window
        slide = [0] * 26
        counter =Counter(s1)
        l,r = 0,0
        n = len(s2)
        m = len(s1)
        while r < n:
            if s2[r] in counter:
                counter[s2[r]] -= 1
                r += 1
            else:
                l = r + 1
            if r - l> m:
                slide[ord(s2[l]) - ord("a")] += 1
                l += 1
            if all(a == 0 for a in slide):
                return True
        return False