# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #this problem we need to use binary tree traverse to solve
        # there are three traverse method: inorder preorder and postorder
        #1, inorder traverse
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        #2, preorder traverse and postorder traverse is not fit for this problem