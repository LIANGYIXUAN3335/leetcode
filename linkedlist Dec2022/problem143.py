class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        NodeList = []
        node = ListNode()
        temp = head
        while temp:
            NodeList.append(head)
            temp = head.next
            head.next = None
            head = temp
        for i in range(0, len(NodeList)//2):
            # print(start)
            node.next = NodeList[i]
            node = node.next
            node.next = NodeList[len(NodeList) - i - 1]
            node = node.next
        if len(NodeList) % 2 == 1 :
            node.next = NodeList[len(NodeList)//2]


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2