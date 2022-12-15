class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxContain = (right - left )* min(height[right],height[left])
        while left < right :
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            cur = (right - left )* min(height[right],height[left])
            maxContain = max(cur, maxContain)
        return maxContain