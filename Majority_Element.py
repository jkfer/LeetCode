# https://leetcode.com/problems/majority-element/
# 169

# Pretty straightforrward if using dictionary to keep count of the elements


class Solution:
    def majorityElement(self, nums):
        D = dict()
        for i in nums:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1

        # find the count that is greater than n
        L = len(nums)
        for a in D:
            if D[a] > int(L/2):
                return a
