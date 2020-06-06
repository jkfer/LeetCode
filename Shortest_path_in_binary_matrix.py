# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# 1091

"""
Provided is a adjacency matrix
BFS
"""

import queue


class Solution:
    def getNeighbours(self, point, grid):
        D = [(0, -1), (0, 1), (1, 0), (1, -1),
             (1, 1), (-1, 0), (-1, -1), (-1, 1)]

        r, c = point
        ANS = []

        for dr, dc in D:
            R = r + dr
            C = c + dc

            if (R < 0 or R >= len(grid)) or \
                    (C < 0 or C >= len(grid[0])):
                continue
            elif grid[R][C] == 0:
                ANS.append([R, C])

        return ANS

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        elif grid == [[0]]:
            return 1

        if grid[0][0] == 1:
            return -1

        Q = []
        Q.append([0, 0])
        steps = 1

        while len(Q) > 0:
            steps += 1
            newQ = []
            for N in Q:
                [r, c] = N
                grid[r][c] = 1
                neighbours = self.getNeighbours([r, c], grid)
                for n in neighbours:
                    if n == [len(grid) - 1, len(grid[0]) - 1]:
                        return steps
                    else:
                        newQ.append(n)
                        a, b = n
                        grid[a][b] = 1
            Q = newQ

        return -1


grid = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid3 = [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 1]]
grid4 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

S = Solution()
ans = S.shortestPathBinaryMatrix(grid4)
print(ans)
