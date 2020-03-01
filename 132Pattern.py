# https://leetcode.com/problems/132-pattern/
# 456
# Medium


import collections


class Solution:
    def eval_stack(stack):
        a, b, c = stack[0], stack[1], stack[2]
        if b > a and c > a and c < b:
            return True
        else:
            return False

    # passes 89/95 test cases
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False

        # create a min array:
        minArray = nums.copy()
        for i, n in enumerate(nums):
            if i == 0:
                minArray[i] = nums[i]
            if i > 0:
                minArray[i] = min(nums[i], minArray[i-1])

        # print(minArray)

        # iterate from reverse:
        for i in range(len(nums) - 1, 0, -1):
            mid = nums[i]
            for n in nums[i+1:]:
                if mid > n and n > minArray[i-1]:
                    return True
        return False


S = Solution()
print(S.find132pattern([1, 2, 3, 4]))
