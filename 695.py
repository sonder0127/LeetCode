class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #O(mn),O(mn)
        m, n = len(grid), len(grid[0])
        self.max_area = 0
        self.area = 0
        def dfs(row, col):
            if row<0 or row>=m or col<0 or col>=n or grid[row][col]!=1:
                return
            grid[row][col] = 2
            self.area += 1
            self.max_area = max(self.max_area, self.area)
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
        return self.max_area