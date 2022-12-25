class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we can also mark the zero col and row in the matrix, 
        # but then we need to classified discussion
        # although space complexity is saved ,but the code looks more complicated
        zeroRol = set()
        zeroCol = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    zeroRol.add(i)
                    zeroCol.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zeroRol or j in zeroCol:
                    matrix[i][j] = 0
        return matrix