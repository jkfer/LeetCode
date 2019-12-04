# 268
# https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums):
        # fastest way to do this will be a Binary search approach:
        nums.sort()
        m = len(nums)
        i = 0

        while i < m:
            if nums[i] != i:
                break
            i += 1

        return i


S = Solution()
print(S.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
