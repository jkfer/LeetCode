# https://leetcode.com/problems/first-bad-version/
# 278
# passed

"""
Idea: To have minimum calls tp isBadVersion - use binary search
"""


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = 1
        L = n
        found = False
        while F <= L and not found:
            M = (L + F) // 2
            if isBadVersion(M):
                if not isBadVersion(M-1):
                    return M
                else:
                    L = M - 1
            else:
                F = M + 1
