class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 100, 4, 200, 1,3,2
        # set(100,4,200,1,3,2)
        # iterate all element and judge if they are the first element of a sequence
        # 1 2 3 4 
        record = set(nums)
        maxlength = 0
        for i in nums:
            if i-1 not in record:
                curlength = 1
                while i+1 in record:
                    curlength += 1
                    i += 1
                maxlength = max(maxlength, curlength)
        return maxlength
        # time complexity = O(n)
        # space complexity = O(n)
                
        