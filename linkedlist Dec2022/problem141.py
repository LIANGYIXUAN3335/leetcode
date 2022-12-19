# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast = head.next
        fast = head # because head can be null so we can not set fast as head.next
        slow = head
        # while fast and slow:
        while fast and fast.next:
            # because fast's initial value is head which is equal to slow,
            # we need to change the value of them at first
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            # fast = fast.next.next
            # slow = slow.next
        return False