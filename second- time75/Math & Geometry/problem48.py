class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left ,right = 0, len(matrix) - 1
        while right > left:
            for i in range(right - left):
                temp = matrix[left][left + i]
                matrix[left][left + i] = matrix[right - i][left]
                matrix[right - i][left] = matrix[right][right - i]
                matrix[right][right - i] = matrix[left + i][right]
                matrix[left + i][right] = temp
            right -= 1
            left += 1