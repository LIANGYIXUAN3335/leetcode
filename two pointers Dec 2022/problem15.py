class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # we sort the array to avoid duplicate element
        nums.sort()
        # we fix i and then use two pointers to solve this problem 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # then we use two pointers to solve this problem
            # if we set right = left + i but this will make the condition more complicated
            left, right = i+1,len(nums) - 1
            while left < right and right < len(nums):
                twosum = nums[left] + nums[right]
                if twosum <=  0 - nums[i]:
                    if twosum == 0 - nums[i]:
                        res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                else :
                    right -= 1
        return res
