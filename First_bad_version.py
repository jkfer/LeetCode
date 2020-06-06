# https://leetcode.com/problems/first-bad-version
# 278


class Solution:
    def firstBadVersion(self, n):
        L = 1
        R = n
        while L <= R:
            M = (L + R) // 2
            if isBadVersion(M) and not isBadVersion(M-1):
                return M
            elif not isBadVersion(M):
                L = M + 1
            else:
                R = M - 1
        return -1
