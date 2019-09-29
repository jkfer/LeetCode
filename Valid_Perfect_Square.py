"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num):
        A = num ** 0.5
        if A.is_integer():
            return True
        else:
            return False
        
S = Solution()
if S.isPerfectSquare(17):
    print('This')