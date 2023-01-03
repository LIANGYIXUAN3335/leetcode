class Solution:
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TO SOLVE THIS PROBlem we need to use inorder tranversal
        # Review: Inorder traversal : left -> root ->right
        # preorder traversal : root -> left -> right
        # postorder traversal : left - > right -> root
        # to finish inorder traverse we can use stack
        res = 0
        def dfs(root):
            nonlocal k ,res
            if not root:
                return
            dfs(root.left)
            if k == 1:
                res = root.val
            k -= 1 
            dfs(root.right)
        dfs(root)
        return res
