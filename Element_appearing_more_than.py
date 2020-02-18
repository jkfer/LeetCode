# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# 1287 - Passed

import collections


class Solution:
    def findSpecialInteger(self, arr):
        D = collections.defaultdict(int)
        N = 0

        for n in arr:
            D[n] += 1
            N += 1

        for n in D.keys():
            if D[n] > N // 4:
                return n
