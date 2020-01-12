# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution:
    def findNumbers(self, nums):
        count = 0
        for N in nums:
            if len(str(N)) % 2 == 0:
                count += 1

        return count
