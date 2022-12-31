class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     dic = {nums[i]:i for i in range(len(nums))}
    #     nums.sort()
    #     left,right = 0, len(nums) - 1
    #     while left < right:
    #         if nums[left] + nums[right] > target:
    #             right -= 1
    #         elif nums[left] + nums[right] < target:
    #             left += 1
    #         else:
    #             return [dic[nums[left]],dic[nums[right]]]
    #             class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
