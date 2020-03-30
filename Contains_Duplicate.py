# https://leetcode.com/problems/contains-duplicate/
# 217


class Solution:
    def containsDuplicate(self, nums):
        D = dict()
        for i in nums:
            if i in D:
                return True
            else:
                D[i] = 1
        return False
