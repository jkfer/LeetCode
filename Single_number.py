# 136
# https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums):
        D = dict()

        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1

        for a, b in D.items():
            if b == 1:
                return a
