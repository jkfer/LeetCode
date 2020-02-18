# https://leetcode.com/problems/duplicate-zeros/


class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(arr)

        ans = []
        for i in range(n):
            ans.append(arr[i])
            if arr[i] == 0:
                ans.append(0)

        for i in range(n):
            arr[i] = ans[i]

        # print(arr)


S = Solution()
S.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
