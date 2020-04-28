#
#

import collections


class Solution:
    def findMaxLength(self, nums):
        count = 0
        D = collections.defaultdict(list)
        for i, n in enumerate(nums):
            if n == 0:
                count -= 1

            if n == 1:
                count += 1

            D[count].append(i)

        # print(D)

        m = 0
        for v in D:
            if v == 0:
                m = max(m, D[v][-1] + 1)
            else:
                m = max(m, D[v][-1] - D[v][0])

        return m


S = Solution()
print(S.findMaxLength([0, 1]))
