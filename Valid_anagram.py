# https://leetcode.com/problems/valid-anagram/
# 242


import collections


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        Ds = collections.defaultdict(int)
        Dt = collections.defaultdict(int)

        for n in s:
            Ds[n] += 1
        for n in t:
            Dt[n] += 1

        for v in Ds.keys():
            if Ds[v] != Dt[v]:
                return False

        return True

    # Better: One dict
    def isAnagram2(self, s, t):
        D = dict()
        for v in s:
            if v in D:
                D[v] += 1
            else:
                D[v] = 1

        for v in t:
            if v not in D:
                return False
            else:
                D[v] -= 1

        for v in D:
            if D[v] != 0:
                return False

        return True
