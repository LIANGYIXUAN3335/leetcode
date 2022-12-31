class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        need = Counter(s)
        for i in t:
            if i in need.keys():
                need[i] = need[i] - 1
            else:
                return False
        for v in need.values():
            if v != 0:
                return False
        return True