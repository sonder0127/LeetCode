class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        vals = []
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        while left<=right and top<=bottom:
            for col in range(left, right+1):
                vals.append(matrix[top][col])
            for row in range(top+1, bottom+1):
                vals.append(matrix[row][right])
            if left<right and top<bottom:
                for col in range(right-1, left-1, -1):
                    vals.append(matrix[bottom][col])
                for row in range(bottom-1, top, -1):
                    vals.append(matrix[row][left])
            left += 1
            right -=1
            top += 1
            bottom -=1
        return vals