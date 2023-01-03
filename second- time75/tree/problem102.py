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
            if len(curlevel) != 0:
                res.append(curlevel)
        return res