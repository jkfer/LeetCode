# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34
# Medium - passed


class Solution:
    def searchRange(self, nums, target):
        # base case:
        if not nums:
            return [-1, -1]

        f_found = l_found = False
        f = ll = None
        F = 0
        L = len(nums) - 1

        while f is None or l is None:
            if f_found is False and nums[F] == target:
                f_found = True
                f = F
            else:
                if F == len(nums) - 1:
                    f = -1
                    f_found = True
                else:
                    F += 1

            if l_found is False and nums[L] == target:
                l_found = True
                ll = L
            else:
                if L == 0:
                    ll = -1
                    l_found = True
                else:
                    L -= 1

        return [f, l]


S = Solution()
print(S.searchRange([5, 7, 7, 8, 8, 10], 6))
