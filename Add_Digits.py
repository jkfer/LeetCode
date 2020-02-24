# https://leetcode.com/problems/add-digits/
# 258


class Solution:
    def addDigits(self, num):
        n = str(num)
        while len(n) > 1:
            N = 0
            for i in n:
                N += int(i)
            n = str(N)

        return n


S = Solution()
print(S.addDigits(38))
