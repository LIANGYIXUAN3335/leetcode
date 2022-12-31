class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if(nums[left] <= nums[right]):
                minNum = min(nums[left],minNum)
                break
            mid = (left + right)//2
            minNum = min(nums[mid],minNum)
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1
        return minNum