# https://leetcode.com/problems/palindrome-number/
# 9


class Solution:
    def isPalindrome(self, x):
        # if x is negative or ends with a 0:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        n = x
        x_rev = 0

        while x > 0:
            lnum = x % 10
            x = x // 10

            x_rev = x_rev*10 + lnum

        return n == x_rev
