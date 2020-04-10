# https://leetcode.com/problems/move-zeroes/
# 283


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums)
        i = 0
        count = 0
        while i < k and count < k:
            count += 1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

    def moveZeroes2(self, nums):
        """
        Get the non zero items to the font of the array
        """
        i = j = 0
        zeros = 0
        # find the fir

        while i < len(nums):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                zeros += 1
            i += 1

        for i in range(len(nums) - 1, len(nums) - 1 - zeros, -1):
            nums[i] = 0

        return nums


S = Solution()
print(S.moveZeroes2([0, 1, 0, 3, 12]))
