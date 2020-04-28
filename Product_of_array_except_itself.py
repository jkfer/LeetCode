# https://leetcode.com/problems/product-of-array-except-self/
# 238
# Medium

import collections
import itertools


class Solution:
    def productExceptSelf(self, nums):
        k = len(nums)
        if k <= 1:
            return nums

        L = [1] * k
        R = [1] * k
        ans = [None] * k

        # traverse right
        for n in range(1, k):
            L[n] = L[n-1] * nums[n-1]

        # print(L)

        # traverse left
        for n in range(k-2, -1, -1):
            R[n] = R[n+1] * nums[n+1]

        # print(R)

        for i in range(k):
            ans[i] = L[i] * R[i]

        return ans


S = Solution()
ans = S.productExceptSelf([1, 2, 3, 4])
print(ans)
