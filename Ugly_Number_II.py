"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

# INCOMPLETE

from fractions import gcd
from sys import maxint


class Solution:
    def nthUglyNumber(self, n):
        res = [1]
        i = j = k = 0
        count = 0
        
        while count < n:
            val = min(res[i]*2,min(res[j]*3,res[k]*5))
            if val == res[i]*2:
                i+=1
            if val == res[j]*3:
                j+=1
            if val == res[k]*5:
                k+=1
            count+=1
            if count == n:
                return res
            res.append(val)

S = Solution()
x = S.nthUglyNumber(6)
print(x)
