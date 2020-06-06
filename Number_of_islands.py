# https://leetcode.com/problems/number-of-islands/
# 200
# Medium


class Solution:
    def countIslands(self, grid, i, j):
        if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0"):
            return 0

        grid[i][j] = "0"

        self.countIslands(grid, i-1, j)
        self.countIslands(grid, i+1, j)
        self.countIslands(grid, i, j-1)
        self.countIslands(grid, i, j+1)

        return 1

    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += self.countIslands(grid, i, j)
        return islands
