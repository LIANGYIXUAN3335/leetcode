# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         sentence = []
#         for i in s:
#             if ord(i) - ord("a") < 26 and ord(i) - ord("a") >= 0 :
#                 sentence.append(i)
#             elif ord(i) - ord("A") < 26 and ord(i) - ord("A") >= 0:
#                 sentence.append(i.lower())
#             elif  ord("9") >= ord(i) >= ord("0"): 
#                 sentence.append(i)
#         left = 0
#         right = len(sentence) -1
#         print(sentence)
#         while left < right:
#             if sentence[left] != sentence[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )