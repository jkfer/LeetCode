# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# 448


import collections


class Solution:
    def findDisappearedNumbers(self, nums):
        D = collections.defaultdict(int)
        for n in nums:
            D[n] += 1

        ans = []
        for n in range(1, len(nums)+1):
            if D[n] == 0:
                ans.append(n)

        return ans

    # better referred solution:
    def findDisappearedNumbers2(self, nums):
        for n in range(len(nums)):
            ind = abs(nums[n]) - 1
            if nums[ind] > 0:
                nums[ind] *= -1

        # print(nums)
        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans


S = Solution()
print(S.findDisappearedNumbers2([4, 3, 2, 7, 8, 2, 3, 1]))
