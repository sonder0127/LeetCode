class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for angle in range(n-1):
            for i in range(angle+1, n):
                matrix[angle][i], matrix[i][angle] = matrix[i][angle], matrix[angle][i]
        
        # for row in range(n):
        #     for i in range(n//2):
        #         matrix[row][i], matrix[row][n-1-i] = matrix[row][n-i-1], matrix[row][i]
        for row in matrix:
            row.reverse()
        

