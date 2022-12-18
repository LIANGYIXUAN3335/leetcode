# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# WE USE TWO POINTERS TO SOLVE THIS PROB 
        curr = head
        pre = None
        while curr :
# BECAUSE WHEN WE POINT TO THE OTHER DIRECTION , WE HAVE NO LINK TO NEXT ,SO WE NEED TO STORE IT BEFORE
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp      
        return pre