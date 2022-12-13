class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in nums:
                end = nums.index(target - nums[i])
                if i != end:
                    ans.append(i)
                    ans.append(end)
                    return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """