class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValid(root,float("-inf"),float("inf"))
    def isValid(self,root,left,right):
            if not root:
                return True
            if root.val >= right or root.val <= left:
                return False
            return self.isValid(root.left, left, root.val) and self.isValid(root.right,root.val,right)