class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isvalid(s) -> bool:
            return ord("a") <= ord(s) <= ord("z") or ord("A") <= ord(s) <= ord("Z") or ord("0") <= ord(s) <= ord("9")
        left , right = 0, len(s)-1
        while(left < right):
            while left < len(s) and not isvalid(s[left]):
                left += 1
            while right >= 0 and not isvalid(s[right]):
                right -= 1
            if left >= len(s) or right<0:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True