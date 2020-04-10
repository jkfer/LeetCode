# https://leetcode.com/problems/happy-number/
# 202

"""
Idea:
Happy number is only possible for n = 1 or
all squares of all the nums add up to 1, 10, 100, 1000, ....

Solution (referred):
when you calculate the sum of n^2 for each number - the sum
should be uniqe each time, if you meet the same sum again,
you will not have the solution you are looking for.
"""


# referred solution
class Solution:
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True
