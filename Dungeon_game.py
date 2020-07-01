# https://leetcode.com/problems/dungeon-game/
# HARD
# 174


# referred solution:
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        R, C = len(dungeon), len(dungeon[0])
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if r == R-1 and c == C-1:
                    dungeon[r][c] = min(dungeon[r][c], 0) * -1 + 1
                elif r == R-1:
                    dungeon[r][c] = max(dungeon[r][c+1] - dungeon[r][c], 1)
                elif c == C-1:
                    dungeon[r][c] = max(dungeon[r+1][c] - dungeon[r][c], 1)
                else:
                    dungeon[r][c] = max(min(dungeon[r][c+1], dungeon[r+1][c]) - dungeon[r][c], 1)
        return dungeon[0][0]


dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
# dungeon = [[-3, 5]]
# dungeon = [[0, -3]]
S = Solution()
print(S.calculateMinimumHP(dungeon))
