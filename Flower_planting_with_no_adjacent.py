# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# 1024


import collections


# referred solution:
class Solution:
    def gardenNoAdj(self, N, paths):
        g = collections.defaultdict(list)
        # the connection is bi-directional:
        for x, y in paths:
            g[x].append(y)
            g[y].append(x)

        # create a preset to save final result:
        plantdict = {i: 0 for i in range(1, N + 1)}

        # print(plantdict)
        # print(g)

        # for each garden:
        for garden in g:
            # answer set to choose from:
            pick = set(range(1, 5))

            # for each connection of the garden
            for each in g[garden]:

                # if the garden already has a color assigned to it
                # and that color is in pick -- exclude that from pick
                # as you cannot choose that
                if plantdict[each] != 0 and plantdict[each] in pick:
                    pick.remove(plantdict[each])

            # out of what is remaining, choose the last
            plantdict[garden] = pick.pop()

        return \
            [plantdict[x] if plantdict[x] != 0 else 1 for x in range(1, N+1)]


L = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
S = Solution()
print(S.gardenNoAdj(4, L))
