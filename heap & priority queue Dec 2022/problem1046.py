class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use min-heap to solve a max-heap problem
        # we just need to multiple -1 foreach element in the list
        stonelist = [-s for s in stones]
        # then we use heapify to make it a minheap
        heapq.heapify(stonelist)
        while(len(stonelist) > 1):
            # get the most heavy two stones
            first = heapq.heappop(stonelist)
            second = heapq.heappop(stonelist)
            cur = first - second
            if cur != 0 :
                heapq.heappush(stonelist,cur)
        stonelist.append(0)
        return abs(stonelist[0])