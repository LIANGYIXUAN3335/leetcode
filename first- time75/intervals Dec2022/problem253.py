class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startlist = sorted([interval[0] for interval in intervals])
        endlist = sorted([interval[1] for interval in intervals])
        i,j = 0, 0
        count = 0
        maxcount = 0
        while i< len(intervals) and j <len(intervals):
            if startlist[i] < endlist[j] :
                count += 1
                i += 1
            elif startlist[i] == endlist[j] :
                i += 1
                j += 1
            else:
                count -= 1
                j += 1
            maxcount = max(count , maxcount)
        return maxcount