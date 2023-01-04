# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = head= ListNode()
        for i in range(len(lists)):
            if lists[i]:
                heap.append([lists[i].val,i])
                lists[i] = lists[i].next
        heapq.heapify(heap)
        while heap:
            cur = heapq.heappop(heap)
            head.next = ListNode(cur[0])
            head = head.next
            if lists[cur[1]]:
                heapq.heappush(heap,[lists[cur[1]].val,cur[1]])
                lists[cur[1]] = lists[cur[1]].next
        return res.next
            