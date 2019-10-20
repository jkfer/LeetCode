# 1228
from collections import Counter


class Solution:
    def missingNumber(self, arr):
        # base case - all elements of the array are the same, diff is 0
        if len(set(arr)) == 1:
            return arr[0] 

        # array length is 3:
        if len(arr) == 3:
            #find if this is increasing or dec:
            incr = True if arr[1] > arr[0] else False
            a, b = arr[1] - arr[0], arr[2] - arr[1]
            if incr:
                return min(arr[:2]) + min([a, b])
            else:
                return max(arr[:2]) + max([a, b])



        D = dict()
        A = [None] * (len(arr) -1)
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            A[i] = diff
            if diff in D:
                D[diff] += 1
            else:
                D[diff] = 1

        for a, b in D.items():
            if b == 1:
                j = A.index(a)
            elif b > 1:
                other_a = a

        # new_arr = arr[:j+1] + [arr[j] + other_a] + arr[j+1:]
        new_arr = arr[j] + other_a
        return new_arr


L = [5, 7, 11, 13]
S = Solution()
x = S.missingNumber(L)
print(x)
