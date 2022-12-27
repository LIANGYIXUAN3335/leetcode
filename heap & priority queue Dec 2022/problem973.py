class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            dist = points[i][0] ** 2 + points[i][1] ** 2
            points[i]= [dist, points[i][0],points[i][1]]
        # heapify a list of list will incording to the first element 
        # heap cost no more memory but sort need memory
        # but a little bit more time than sort
        heapq.heapify(points)
        for j in range(k):
            res.append(heapq.heappop(points)[1:3])
        return res