class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxvalue = float('-inf')
        def dfs(root):
            if not root:
                return 0
            nonlocal maxvalue
            curleft = max(0,dfs(root.left))
            curright = max(0,dfs(root.right))
            maxvalue = max(maxvalue, curleft + curright + root.val)
            return max(curleft,curright) + root.val
        dfs(root)
        return maxvalue