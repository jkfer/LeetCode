# https://leetcode.com/problems/array-nesting/
# Medium


class Solution:
    def arrayNesting(self, nums):
        m = 0
        D = [False] * len(nums)

        for i in nums:
            j = i
            count = 0
            while not D[j]:
                D[j] = True
                count += 1
                j = nums[j]
            m = max(count, m)

        return m


S = Solution()
L = S.arrayNesting([5, 4, 0, 3, 1, 6, 2])
X = S.arrayNesting([0, 2, 1])
print(L)
print(X)
