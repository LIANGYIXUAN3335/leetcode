class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        res = []
        # use sort and lambda to sort an list with element list
        intervals.sort(key = lambda pair : pair[0])
        while i < len(intervals):
            cur = intervals[i]
            while i + 1 < len(intervals) and cur[1] >= intervals[i+1][0]:
                i += 1
                cur[1] = max(intervals[i][1],cur[1])
            i += 1
            res.append(cur)
        return res
            
                
