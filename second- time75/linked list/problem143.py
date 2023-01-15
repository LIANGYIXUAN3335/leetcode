class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle listNode
        # reverse the second list

        slow, fast = head,head
        if not fast.next:
            return head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        temp.next = None
        cur = slow
        pre = None
        while cur :
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        list1 = head
# when we merge two linked list, the first link longer will be easier to process
        while pre and list1:
            temp1 = list1.next
            list1.next = pre
            temp2 = pre.next
            pre.next = temp1
            temp3 = pre
            list1 = temp1
            pre = temp2
        if pre :
            temp3.next = pre
        return head