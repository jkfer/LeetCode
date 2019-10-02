"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0, 1, 2]

        # Base case:
        if n < 3:
            return res[n]

        # res[3] = (ways to climb 2) res[2] + (ways to climb 1) res[1] = 3
        # res[4] = (ways to climb 3) res[3] + (ways to climb 2) res[2] = 4
        # res[5] = res[4] + res[3]
        # res[6] = res[5] + res[4]

        for n in range(3, n + 1):
            R = res[n-1] + res[n-2]
            res.append(R)
        
        return res[n]

S = Solution()
print(S.climbStairs(10))