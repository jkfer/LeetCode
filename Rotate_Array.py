# 189
# https://leetcode.com/problems/rotate-array/


class Solution:
    # Solution exceeds time limit
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            last = nums[-1]
            for i in range(len(nums)-1)[::-1]:
                nums[i+1] = nums[i]
            nums[0] = last

        print(nums)

    # passed solution - good complexity
    def rotate2(self, nums, k):
        k = k % len(nums)
        last = nums[:len(nums) - k]
        first = nums[-k:]

        for i in range(len(nums)):
            if i < k:
                nums[i] = first.pop(0)
            else:
                nums[i] = last.pop(0)

        return nums


S = Solution()
print(S.rotate2([1, 2, 3, 4, 5, 6, 7], 3))
