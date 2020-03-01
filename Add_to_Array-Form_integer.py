# https://leetcode.com/problems/add-to-array-form-of-integer/
# 989


class Solution:
    def addToArrayForm(self, A, K):
        X = int("".join(list(map(str, A)))) + K
        return list(map(int, str(X)))
