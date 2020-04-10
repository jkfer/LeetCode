# 136
# https://leetcode.com/problems/single-number/
"""
Note: for this you can consider the XOR operation (^=)
n xor n = 0
0 xor n = n
if you keep xoring each number with n, we will get the number that is single.
"""

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

    def singleNumber2(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans