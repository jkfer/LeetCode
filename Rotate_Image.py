# 48
# In the resulting array the ith  column is the ith row
# This will be easy to do the zip


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = len(matrix) - 1
        row = len(matrix[0])

        ref_array = matrix.copy()

        for i in range(row):
            matrix[i] = [ref_array[j][i] for j in range(column, -1, -1)]

        # return matrix


S = Solution()
S.rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
