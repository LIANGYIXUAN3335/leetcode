class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap +  heap
        ans = {}
        for i in nums:
            ans[i] = ans.get(i,0) + 1
        heap = []
        for key in ans.keys():
            heapq.heappush(heap,[ans[key],key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]