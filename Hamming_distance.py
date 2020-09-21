# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x, y):
        ans = 0
        for _ in range(32):
            if x & 1 != y & 1:
                ans += 1
            x >>= 1
            y >>= 1
        return ans
