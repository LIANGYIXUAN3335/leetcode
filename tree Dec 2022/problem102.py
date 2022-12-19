# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        curlist = deque()
        curlist.append(root)
        while len(curlist) != 0:
            curlevel = []
            for i in range(len(curlist)):
                curnode = curlist.popleft()
                if curnode:
                    curlist.append(curnode.left)
                    curlist.append(curnode.right)
                    curlevel.append(curnode.val)
            print(curlevel)
            if len(curlevel) != 0:
                res.append(curlevel)
        return res