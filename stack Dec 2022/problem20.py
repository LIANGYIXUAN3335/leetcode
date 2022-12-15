class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i in {"(","[","{"}:
                stack.append(i)
            elif len(stack) ==0:
                return False
            else:
                if i == ")" and stack.pop() != "(":
                    return False
                elif i == "]" and stack.pop() != "[":
                        return False
                elif i == "}" and stack.pop() != "{":
                        return False
        if len(stack) ==0:
            return True
        else:
            return False
                    