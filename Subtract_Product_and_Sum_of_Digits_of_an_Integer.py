# https://leetcode.com/contest/weekly-contest-166/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# passed


class Solution:
    def subtractProductAndSum(self, n):
        p = 1
        s = 0
        for i in str(n):
            if p != 0:
                p *= int(i)
            s += int(i)

        return p - s


S = Solution()
print(S.subtractProductAndSum(234))
