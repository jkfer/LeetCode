"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

nums = [1,3,5,6]
target = 0

class Solution:
    def searchInsert(self, nums, target):
        j = 0
        for i in range(len(nums)):
            if target > nums[i]:
                j += 1
        print(j)

S = Solution()
S.searchInsert(nums, target)

