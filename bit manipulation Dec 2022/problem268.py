class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNum = (1 + len(nums)) * len(nums) // 2
        for i in nums:
            sumNum -= i
        return sumNum