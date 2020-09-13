# https://leetcode.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid):
        if grid == [[1]]:
            return 4

        # visited = [[False for _ in range(len(grid[0]))]
        # for _ in range(len(grid))]
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # and not visited[i][j]:
                    perimeter += 4
                    # visited[i][j] = True
                    # inspect the surroundings:

                    D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in D:
                        R = i + dr
                        C = j + dc

                        neighbours = 0
                        if (R >= 0 and R < len(grid)) and \
                                (C >= 0 and C < len(grid[0])):
                            if grid[R][C] == 1:
                                # neighbours += 1
                                # visited[R][C] = True
                                perimeter = perimeter - 1

                        # perimeter -= (2 * neighbours)

        return perimeter

    # referred solution - a bit faster
    def islandPerimeter2(self, grid):
        def getPerim(i, j):
            if (0 <= i < len(grid)) and (0 <= j < len(grid[i])):
                if grid[i][j] == 1:
                    return 0
            return 1

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += getPerim(i-1, j)
                    count += getPerim(i+1, j)
                    count += getPerim(i, j-1)
                    count += getPerim(i, j+1)
        return count


S = Solution()
L = [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
print(S.islandPerimeter(L))
