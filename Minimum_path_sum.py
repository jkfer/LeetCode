# https://leetcode.com/problems/minimum-path-sum/
# Medium


import sys


L = [
    [1, 4, 8, 6, 2, 2, 1, 7],
    [4, 7, 3, 1, 4, 5, 5, 1],
    [8, 8, 2, 1, 1, 8, 0, 1],
    [8, 9, 2, 9, 8, 0, 8, 9],
    [5, 7, 5, 7, 1, 8, 5, 5],
    [7, 0, 9, 4, 5, 6, 5, 6],
    [4, 9, 9, 7, 9, 1, 9, 0]
]

K = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]


# referred Errichto DP solution
class Solution:
    def minPathSum(self, grid):
        # start:
        row = len(grid)
        col = len(grid[-1])
        DP = [[0 for i in range(col)] for i in range(row)]

        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    DP[0][0] = grid[0][0]
                else:
                    DP[r][c] = grid[r][c] + min(DP[r][c-1] if c != 0 else sys.maxsize, DP[r-1][c] if r != 0 else sys.maxsize)

        return DP[row-1][col-1]


S = Solution()
print(S.minPathSum(K))
