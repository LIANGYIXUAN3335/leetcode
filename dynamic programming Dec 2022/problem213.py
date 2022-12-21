class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 4 3 5 6 1 3 
        # i  
        # 2 4    
        # k (max 1 to k will be x) maxk 
        # k + 1  rob house k + 1 
        # maxk+1 = max(nums[k + 1] + maxk-1 ,maxk )
        def robLinear(nums):
            rob0 = 0
            rob1 = 0
            for i in nums:
                temp = max(rob0 + i, rob1)
                rob0 = rob1
                rob1 = temp
            return max(rob0, rob1)
        # time - O(n)
        # space  - O(1)
        return max(robLinear(nums[0:len(nums) - 1]) ,robLinear(nums[1:]))
        