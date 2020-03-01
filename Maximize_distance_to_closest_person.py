# https://leetcode.com/problems/maximize-distance-to-closest-person/
# 849


class Solution:
    def maxDistToClosest(self, seats):
        D = []
        c = 0
        for i, n in enumerate(seats):
            if n == 1:
                D.append(i)
            c += 1

        m = 0

        if 0 not in D:
            m = max(m, D[0])

        if c-1 not in D:
            m = max(c-1 - D[-1], m)

        # print(D)

        for i in range(1, len(D)):
            m = max((D[i] - D[i-1])//2, m)

        print(m)


S = Solution()
S.maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
