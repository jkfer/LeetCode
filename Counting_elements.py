# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
#


import collections


class Solution:
    def countElements(self, arr):
        D = collections.defaultdict(int)
        for n in arr:
            D[n] += 1

        ANS = 0

        for n in arr:
            if D[n+1] > 0:
                ANS += 1

        return ANS
