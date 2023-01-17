class Solution:
    def minWindow(self, s: str, t: str) -> str:
        diction = {}
        for i in t : 
            diction[i] = diction.get(i,0) + 1
        windic = {}
        need = len(diction)
        have = 0
        res = ""
        length = float("inf")
        left = 0
        for right in range(len(s)):
            if s[right] in diction: # CS
                windic[s[right]] = windic.get(s[right],0) + 1
                if windic[s[right]] == diction[s[right]]:
                    have += 1
            while have ==  need:
                # print(s[left:right + 1])
                if right - left < length:
                    res = s[left:right + 1]
                    length = right - left +1
                if s[left] in diction:
                    if windic[s[left]] == diction[s[left]]:
                        have -= 1
                    windic[s[left]] -= 1
                left += 1
        return res
        # time complexity o(C|S| + |T|)
        # SPACE COMPLEXITY (O(C)) A: 1 B : 2 ABB


        