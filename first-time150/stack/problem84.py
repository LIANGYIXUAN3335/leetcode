class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        curMaxArea = 0 
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                curMaxArea = max(stack[-1][1] * (i - stack[-1][0]),curMaxArea)  
                start = stack.pop()[0]
            stack.append((start,heights[i]))
        while stack:
            curMaxArea = max(stack[-1][1] * (len(heights) - stack[-1][0]),curMaxArea)
            stack.pop()
        return curMaxArea
        # O(N)
        # O(N)