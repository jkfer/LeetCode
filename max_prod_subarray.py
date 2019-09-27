"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        max_dp = [0]*len(nums)
        min_dp = [0]*len(nums)
        max_dp[0], min_dp[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
        return max(max_dp + min_dp)


S = Solution()
x = S.maxProduct([-2,3,-4])
print(x)