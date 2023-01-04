class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for start in range(len(nums) - 2):
            if start and nums[start] == nums[start - 1]:
                continue
            left = start + 1
            right = len(nums) - 1
            while left < right:
                if left > start + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                twosum = nums[left] + nums[right]
                if  twosum > (-1) * nums[start]:
                    right -= 1
                elif twosum < (-1) * nums[start]:
                    left += 1
                else:
                    res.append([nums[start],nums[left],nums[right]])
                    right -= 1
                    left += 1
        return res