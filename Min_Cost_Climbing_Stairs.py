"""
746.
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15

Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6

Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

IDEA:
DP:
cost[i] = cost[i] + min(cost[i-1], cost[i-2])

the cost for a stair starting from index 2 will be the sum of the cost to reach there, and then leave from there
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
x = S.minCostClimbingStairs([0,2,2,1])
print(x)
