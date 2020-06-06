# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Medium


class Solution:
    def singleNonDuplicate(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        i = 0
        while i < n:
            if i == n-1:
                return nums[i]

            if nums[i] != nums[i+1]:
                return nums[i]

            # get slow and fast:
            N = nums[i]
            while i+1 < n and nums[i+1] == N:
                i += 1
            i += 1
