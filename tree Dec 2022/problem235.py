# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the point of this problem is that the left node are alwarys lower than that root and right nodes are always higher
        while root:
            if root.val - p.val >0 and root.val - q.val >0 :
                root = root.left
            elif root.val - p.val <0 and root.val - q.val <0 :
                root = root.right
            else:
                return root