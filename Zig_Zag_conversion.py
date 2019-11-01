# 6

"""
# Tough:
Idea was to generate a list that is of length of s but consist only the row
numbers that each char of s should go into. This will help with seperating
the charachters into group. Iterate through s, seperate chars.
then join the seperated chars in row number order.
"""


class Solution:
    def convert(self, s, numRows):
        if len(s) < numRows or numRows == 1:
            return s

        R = range(numRows) + range(numRows - 2, 0, -1)

        D = dict()
        for i in range(numRows):
            D[i] = ""

        # Generate a list R of the length for the array:
        RR = R * (len(s) / len(R))
        RR += R[:len(s) % len(R)]

        for a, b in zip(RR, s):
            D[a] += b

        ans = ""
        for r in range(numRows):
            ans += D[r]

        return ans


S = Solution()
print(S.convert('PAYPALISHIRING', 3))
