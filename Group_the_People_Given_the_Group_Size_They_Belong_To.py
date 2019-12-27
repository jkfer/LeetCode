# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# 1282
# Medium - passed

"""
Introduce a dict to keep count of the groups and its members.
"""


class Solution:
    def groupThePeople(self, groupSizes):
        # travers the input list
        D = dict()

        for i, num in enumerate(groupSizes):
            if num not in D:
                D[num] = [i]
            else:
                D[num].append(i)

        ANS = []

        for key, values in D.items():
            if key == len(values):
                ANS.append(values)
            else:
                for j in range(0, len(values), key):
                    ANS.append(values[j:j+key])

        return ANS


S = Solution()
print(S.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
