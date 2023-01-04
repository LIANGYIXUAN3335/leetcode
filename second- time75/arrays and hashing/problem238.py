class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix [1,1,2,6]
        # postfix [24,12,4,1]
        # res [24,12,8,6]
       
        # res[k] *= postfix[k + 1]
        res =[1] * len(nums)
        for i in range(1,len(nums)):
              # res[k] = prefix[k-1]
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums)-2,-1,-1):
            postfix = nums[i + 1] * postfix
            res[i] = res[i] * postfix
        return res