class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n = 3 leftparentheses = 3 curleftparentheses = 0
#       (((        leftparentheses = 0 curleftparentheses = 3   ---res + 1
#       (()(       leftparentheses = 0 curleftparentheses = 2   ---res + 1
#       (())(      leftparentheses = 0 curleftparentheses = 0  ---res + 1
#       ()        leftparentheses = 2 curleftparentheses = 0  
        # res = [] #2^n
        # curlist = []
        # def dfs(curlist,leftparentheses,notClosedleft):
        #     if leftparentheses == 0:
        #         temp = curlist.copy()
        #         temp += [")"] * notClosedleft
        #         res.append("".join(temp))
        #     elif notClosedleft == 0:
        #         temp = curlist.copy()
        #         temp.append("(")
        #         dfs(temp,leftparentheses - 1,notClosedleft + 1)
        #     else:
        #         temp = curlist.copy()
        #         temp.append("(")
        #         dfs(temp,leftparentheses - 1,notClosedleft + 1)
        #         temp = curlist.copy()
        #         temp.append(")")
        #         dfs(temp,leftparentheses,notClosedleft - 1)
        # dfs([],n,0)
        # return res
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def dfs(path,left,right):
            if left == right and left ==0:
                ans.append(path)
                return
            if left>right :
                return
            if left > 0:
                dfs(path+"(",left -1, right)
            if right > 0:
                dfs(path+")",left, right -1 )
        if n ==0:
            return "[]"
        else:
            dfs("",n,n)
        return ans

