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

Hint:
Write a function f(k) to determine how many ugly numbers smaller than k. As f(k) is non-decreasing, try binary search.

"""



class Solution:
    # return how many ugly numbers are smaller than k
    def count_ugly(self, start, end, a, b, c):
        count = 0
        while start <= end:
            if start % a == 0 or start % b == 0 or start % c == 0:
                count += 1
            start += 1

        return count
    
    def basecheck(self, n, end, a, b, c):
        # return True if there could be an ugly number within the given range:
        pass
    
    def generate_seq(self, start, end, a, b, c):
        K = a*b*c
        L = []
        for l in [a, b, c]:
            L += range(start, K+1, l)
        
        return list(set(L))


    def nthUglyNumber(self, n, a, b, c):
        # generate the seq:
        L = self.generate_seq(a, b, c)
        
        
        