"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.
Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984

Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]


Hint:
Write a function f(k) to determine how many ugly numbers smaller than k. As f(k) is non-decreasing, try binary search.

# LCM - lowest common multiplier of a and b
The lowest number that is devisible by both a and b
this is calculated by = a*b / gcd(a, b)

# GCD - greatest common denominator of a and b
The biggest number that can divide a and b without any remander

"""

from fractions import gcd

class Solution:
    def lcm(self, a, b):
        return a*b // gcd(a, b)

    # return how many ugly numbers are smaller or equal to k
    def count_ugly(self, k, a, b, c, ab, bc, ac, abc):
        ans = k // a + k // b + k // c - (k // ab + k // bc + k // ac) + k // abc
        return ans
    

    def nthUglyNumber(self, n, a, b, c):
        ab, bc, ac = self.lcm(a, b), self.lcm(b, c), self.lcm(a, c)
        abc = self.lcm(ab, c)
        # It's guaranteed that the result will be in range [1, 2 * 10^9]

        start = 1
        end = 2 * 10 ** 9

        while start < end:
            H = start + (end - start) // 2
            if self.count_ugly(H, a, b, c, ab, bc, ac, abc) < n:
                start = H + 1
            else: # case where mid number H has smaller ugly numbers than n
                # you have to move mid to the right then
                end = H
        
        return start
                
S = Solution()
a = S.nthUglyNumber(1000000000, 2, 217983653, 336916467)
print(a)