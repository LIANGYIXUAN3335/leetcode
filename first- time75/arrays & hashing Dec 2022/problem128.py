class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort() # we can not use sort because it cost O(nlog(n))
        setNums = set(nums)
        max = 1
        for i in setNums:
            if i - 1 not in setNums:
                length = 1
                start = i
                while start + 1 in setNums:
                    length += 1
                    start += 1
                if length > max:
                    max = length
        return max