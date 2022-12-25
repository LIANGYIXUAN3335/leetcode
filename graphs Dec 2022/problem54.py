class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0,len(matrix)
        left, right = 0, len(matrix[0])
        ans = []
        while top < bottom and left < right:
            # traverse the element in the top row
            for i in range(left,right,1):
                ans.append(matrix[top][i])
            top += 1
            # traverse the element in the right col
            for i in range(top,bottom):
                ans.append(matrix[i][right - 1])
            right -= 1
            if (not top< bottom) or (not left < right):
                break
            # traverse the element in the bottom row
            for i in range(right - 1,left - 1,-1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1
            # traverse the element in the left col
            for i in range(bottom - 1,top - 1,-1):
                ans.append(matrix[i][left])
            left += 1
        return ans
