# https://leetcode.com/problems/power-of-two/
# 231

# hint: think about  bit manipulation here


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        k = 1

        while k != n and k < n:
            k *= 2
            # print(k)

        if k == n:
            return True
        else:
            return False


S = Solution()
print(S.isPowerOfTwo(64))
