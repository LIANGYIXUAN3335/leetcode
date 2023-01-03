class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None
        temp = root.left
        # TreeNode class have no function invertTree. So we need to use self. to call it
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root