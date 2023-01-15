class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        minval = nums[0]
        while left <= right :
            if nums[left] <= nums[right]:
                return min(minval,nums[left])
            mid = (left + right)//2
            minval = min(nums[mid],minval)
            if nums[mid] > minval :
                left = mid + 1
            else :
                right = mid - 1
        return min(minval,nums[right])