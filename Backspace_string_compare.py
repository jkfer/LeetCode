# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/
#


class Solution:
    def backspaceCompare(self, S, T):
        SS = []
        TT = []

        for n in S:
            if SS and n == "#":
                SS.pop()
            elif n != "#":
                SS.append(n)

        for n in T:
            if TT and n == "#":
                TT.pop()
            elif n != "#":
                TT.append(n)

        return SS == TT
