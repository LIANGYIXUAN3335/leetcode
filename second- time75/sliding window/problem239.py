class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heapqueue/ priority queue
        # (num[i],i) i >= right - k
        # log(k)n 
        # o(k)
        # single 
        # [1,3,-1,-3,5,3,6,7]
        # [1,2,3] num[i] decreasing
        q = collections.deque()
        r = 0
        res = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            r += 1
            if q[0] < r - k:
                q.popleft() 
            if r >= k:
                res.append(nums[q[0]])
        return res