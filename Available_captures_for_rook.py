# https://leetcode.com/problems/available-captures-for-rook/
# 999
"""
Whites - uppercase
blacks - lowercase

white rook - 'R'
black pawn - 'p'

Idea:
find the position of Rook (r,c)
on the same row, to the left and right
    find if there are any direct pawns
for all other rows:
    check if there a pawn on c
    and no other whites between the rook and pawn

find the pawns that are direcly N,S,E,W of the Rook
"""


class Solution:
    def numRookCaptures(self, board):
        R = 0
        C = 0
        # find the R, C of Rook
        while "R" not in board[R]:
            R += 1

        while board[R][C] != "R":
            C += 1

        # get the column of C
        col = [board[r][C] for r in range(8)]
        row = board[R]

        col = "".join(col).replace(".", "")
        row = "".join(row).replace(".", "")

        # count all the Rp and pR in row and column:
        ans = col.count('pR') + col.count('Rp') + \
            row.count('pR') + row.count('Rp')

        return ans


L = [[".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", "R", ".", ".", ".", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "p", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]]
S = Solution()
ans = S.numRookCaptures(L)
print(ans)
