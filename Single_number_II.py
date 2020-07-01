# https://leetcode.com/problems/single-number-ii/
# 137


# referred solution - need clarity:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = 0
        pre_one = pre_two = pre_three = 0

        for n in nums:
            one = (pre_one ^ n)
            two = (pre_one & n) | two
            three = (one & two)

            one &= ~three
            two &= ~three

            # -----
            pre_one = one
            pre_two = two
            pre_three = three

        return one

    # if numbers are all > 0
    def singleNumber2(self, nums):
        n = len(nums)
        ans = 0

        for i in range(32):
            t = 0
            for j in range(n):
                t += (nums[j] & 1)
                nums[j] >>= 1

            t %= 3
            ans += t * pow(2, i)

        return ans


L = [2, 2, 3, 2]
S = Solution()
print(S.singleNumber2(L))
