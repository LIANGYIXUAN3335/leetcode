class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair : pair[0])
        count,i = 0,0
        while i < len(intervals):
            cur = intervals[i]
            while i + 1 < len(intervals) and cur[1] > intervals[i + 1][0]:
                count += 1
                cur[1] = min(intervals[i+1][1], cur[1])
                i += 1
            i += 1
        return count