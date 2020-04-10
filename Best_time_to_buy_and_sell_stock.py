# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121


class Solution:
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for n in prices:
            minprice = min(minprice, n)
            if n - minprice > maxprofit:
                maxprofit = n - minprice
        return maxprofit


S = Solution()
print(S.maxProfit([7, 1, 5, 3, 6, 4]))
