"""
746.
IDEA:
DP:
cost[i] = cost[i] + min(cost[i-1], cost[i-2])

the cost for a stair starting from index 2 will be the sum of the cost to
reach there, and then leave from there
cost to reach index i => min(cost[i-1], cost[i-2])
cost to leave index i => cost[i]
total cost of index i => cost[i] = cost[i] + min(cost[i-1], cost[i-2])
"""


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # Linear
        # start from the min of the first two items:
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])


S = Solution()
x = S.minCostClimbingStairs([0, 2, 2, 1])
print(x)
