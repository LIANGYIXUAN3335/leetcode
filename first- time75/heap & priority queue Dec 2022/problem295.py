class MedianFinder:

    def __init__(self):
        # small is a maxheap and large is a minheap
        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        # we need to decide where should we put num
        if not self.large:
            heapq.heappush(self.large, num)
        elif self.large[0] > num:
            heapq.heappush(self.small, -num)
        else :
            heapq.heappush(self.large, num)
        if len(self.small) - len(self.large) > 1:
            cur = (-1) * heapq.heappop(self.small)
            heapq.heappush(self.large, cur)
        elif len(self.small) - len(self.large) < -1:
            cur = heapq.heappop(self.large)
            heapq.heappush(self.small, -cur)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1) * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((-1) * self.small[0] + self.large[0]) / 2
