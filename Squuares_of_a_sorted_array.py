# https://leetcode.com/problems/squares-of-a-sorted-array/
# 977


class Solution:
    def sortedSquares(self, A):
        A = [n ** 2 for n in A]
        return sorted(A)


S = Solution()
print(S.sortedSquares([-4, -1, 0, 3, 10]))
