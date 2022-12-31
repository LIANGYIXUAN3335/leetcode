# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     #first: I wonder is the tree have the same element,
    #     # assume that all element value is unique
    #     node = deque()
    #     node.append(root)
    #     while len(node) != 0:
    #         head = node.popleft()
    #         if not head:
    #             continue
    #         if head.val == subRoot.val and self.isSameTree(head,subRoot): 
    #             return True
    #         node.append(head.left)
    #         node.append(head.right)
    #     return False
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
