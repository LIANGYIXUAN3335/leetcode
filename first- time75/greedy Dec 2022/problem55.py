# class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     res = [False] * len(nums)
    #     res[-1] = True
    #     for i in range(len(nums) - 2, -1, -1):
    #         for j in range(i+1 , i+ nums[i] + 1 ,1):
    #             if j >= len(nums) or res[j] == True :
    #                 res[i] = True
    #     return res[0]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0