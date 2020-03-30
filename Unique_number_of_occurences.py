# https://leetcode.com/problems/unique-number-of-occurrences/
# 1207

import collections


class Solution:
    def uniqueOccurrences(self, arr):
        D = collections.defaultdict(int)
        for n in arr:
            D[n] += 1

        K = dict()
        for n in D.values():
            if n not in K:
                K[n] = 1
            else:
                return False

        return True
