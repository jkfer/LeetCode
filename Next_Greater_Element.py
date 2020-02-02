# https://leetcode.com/problems/next-greater-element-i/
# 496


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        L = len(nums2)
        D = {p: i for i, p in enumerate(nums2)}
        ANS = [-1] * len(nums1)

        for i, n in enumerate(nums1):
            for k in nums2[D[n]+1:L]:
                if k > n:
                    ANS[i] = k
                    break

        return ANS


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# Ans: [-1, 3, -1]

S = Solution()
print(S.nextGreaterElement(nums1, nums2))
