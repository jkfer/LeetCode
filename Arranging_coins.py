# https://leetcode.com/problems/arranging-coins/
# 441


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n in [0, 1]:
            return n

        stairs = 0
        while n > stairs:
            stairs += 1
            n -= stairs

        return stairs


S = Solution()
print(S.arrangeCoins(6))
