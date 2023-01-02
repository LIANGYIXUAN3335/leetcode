class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheseMap = {"}" : "{", "]":"[",")":"("}
        for i in s:
            if i not in parentheseMap:
                stack.append(i)
                continue
            if not stack or stack.pop() != parentheseMap[i]:
                return False
        return not stack