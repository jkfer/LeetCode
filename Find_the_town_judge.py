# https://leetcode.com/problems/find-the-town-judge/
# 997


import collections


class Solution:
    def findJudge(self, N, trust):
        itrust = collections.defaultdict(list)
        i_being_trusted_by = collections.defaultdict(int)
        for L in trust:
            person, t = L
            itrust[person].append(t)
            i_being_trusted_by[t] += 1

        # judge trusts no-one, so itrust[judge] is []
        # Everyone trust judge so len(i_being_trusted_by[judge]) = N-1
        for i in range(1, N+1):
            if not itrust[i] and i_being_trusted_by[i] == N-1:
                return i

        return -1

    # referred solution - you can use a count array
    def findJudge2(self, N, trust):
        trusted = [0] * (N+1)
        for person, trust in trust:
            trusted[trust] += 1
            trusted[person] -= 1

        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i

        return -1
