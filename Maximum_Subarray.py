"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    # not good for longer input arrays. It will time out.
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        ans = None

        for i, num in enumerate(nums):
            j = i + 1
            while j <= len(nums):
                res = sum(nums[i:j])
                if ans == None:
                    ans = res
                elif res > ans:
                    ans = res
                j += 1
                print(ans)
        print(ans)


    # using Kandanes algo:
    def maxSubArray2(self, nums):
        # base case - if all the input nums are less than 0
        if all(i < 0 for i in nums):
            return max(nums)

        sum_so_far = fin = 0
        
        for i in range(len(nums)):
            # 1. Calculate the sum_so_far
            sum_so_far = sum_so_far + nums[i]
            
            # 2. At any point if the sum_so_far gets less than 0
            # reset it back to 0. WHY ?
            # is we are in this section, all numbers in input array are not minus. there is a num that is greater than 0
            # that number alone will defeat the sum_so_far that is < 0
            if sum_so_far < 0:
                sum_so_far = 0
            
            # set fin to sum_so_far
            if fin < sum_so_far:
                fin = sum_so_far

        return fin

    # Dynamic programming approach
    def maxSubArray3(self, nums):
        # create an array as same length as nums:
        D = [0] * len(nums)
        D[0] = nums[0]
        for i in range(1, len(nums)):
            D[i] = max(D[i-1]+nums[i], nums[i])
        return max(D)




S = Solution()
x = S.maxSubArray3([2,3,-2,4])

print(x)