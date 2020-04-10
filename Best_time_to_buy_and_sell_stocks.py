# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
# 122
"""
find a valley. after that valley - find the next biggetst peak
add the difference to the profit
"""


class Solution:
    def maxProfit(self, prices):
        # using the peak - valley method:
        peak = 0
        valley = 0
        i = 0
        profit = 0

        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # find the next biggest peak:
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            profit += (peak - valley)

        return profit


S = Solution()
print(S.maxProfit([7, 1, 5, 3, 6, 4]))
