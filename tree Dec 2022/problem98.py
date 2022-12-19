# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.isValid(root,float("-inf"),float("inf"))
#     def isValid(self, root: Optional[TreeNode],min,max) -> bool:
#         if not root:
#             return True
#         if root.left:
#             if root.left.val <= min or root.left.val >= max or root.left.val >= root.val:
#                 return False
#         if root.right:
#             if root.right.val >= max or root.right.val <= min or root.right.val <= root.val:
#                 return False
#         return self.isValid(root.left,min,root.val) and self.isValid(root.right,root.val,max)
# remember: when we use recursion we dont need to compare the value of root.left or root.right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))