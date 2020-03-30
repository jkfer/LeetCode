# https://leetcode.com/problems/maximum-69-number/
# 1323


class Solution:
    def maximum69Number(self, num):
        L = list(str(num))
        for i, n in enumerate(L):
            if n == "6":
                L[i] = "9"
                break
        return int("".join(L))
