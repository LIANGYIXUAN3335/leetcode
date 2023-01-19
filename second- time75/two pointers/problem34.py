# class Solution:
#     def trap(self, height: List[int]) -> int:
#         # [0,1,0,2,1,0,1,3,2,1,2,1]
#         # min(left boundary, right boundary) -  curheight = the water current position can trap
#         n = len(height)
#         rightboundary = [0] * n
#         res = 0
#         leftboundary = height[0]
#         rightboundary[-1] = height[-1] 
#         for i in range(1 ,n):
#             rightboundary[n - i - 1] = max(rightboundary[n - i],height[n - i - 1])
#         for i in range(1,n-1):
#             minboundary = min(leftboundary,rightboundary[i + 1])
#             leftboundary = max(leftboundary, height[i])
#             if height[i] < minboundary:
#                 res += minboundary - height[i] 
#         return res
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res