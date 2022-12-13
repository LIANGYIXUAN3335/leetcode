class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashset = list(s)

        for i in t:
            if i in hashset:
                hashset.remove(i)
            else:
                return False
        return True