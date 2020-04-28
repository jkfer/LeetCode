# https://leetcode.com/problems/number-of-1-bits/
# 191

"""
Idea:
Do a shift and bitwise operation on n
n >> 3 is n // 2 ** 3
n & 1 is 1 only if corresponding numbers are 1
ex: 1100 & 1 is 1100 & 0001 which is 0
0001 & 1 is 1

so we take the num and keep dividing it with checking if the last bit is one
"""


# referred solution:
class Solution:
    def hammingWeight(self, n):
        return sum((n >> i & 1 for i in range(32)))

    # alternate
    def hammingWeight(self, n):
        return bin(n).count('1')
