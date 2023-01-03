class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
    #  stack dfs
        stack  = []
        maxlevel = 0
        if not root:
            return 0
        stack.append([root,1])
        while stack:
            curr = stack.pop()
            if curr[0] and curr[0].left:
                stack.append([curr[0].left,curr[1] + 1])
            if curr[0] and curr[0].right:
                stack.append([curr[0].right,curr[1] + 1])
            maxlevel = max(maxlevel,curr[1])
        return maxlevel