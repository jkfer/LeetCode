# https://leetcode.com/problems/advantage-shuffle/
# 870
# Medium

'''
# referred solution:
sort and reverse B.
sort A
for every element of B, if A[-1] > b - then b will take A.pop()
'''
import collections


class Solution:
    # not accurate
    def advantageCount0(self, A, B):
        R = []
        n = len(A)

        for i in range(n):
            j = i
            while j < n and A[j] <= B[i]:
                j += 1

            if j != n:
                a = A[i]
                b = A[j]

                A[i] = b
                A[j] = a

        print(A)

    # referred solution:
    def advantageCount(self, A, B):
        # create a dictionary of list values
        D = collections.defaultdict(list)
        A.sort()

        # for each item in B from biggest to smallest:
        for b in sorted(B)[::-1]:
            # if the number is smaller than biggest of A
            # why? - Identify A's that would match with particular b,
            # So in future we will know if b has a valid match
            if b < A[-1]:
                D[b].append(A.pop())

        ANS = []

        for b in B:
            if D[b]:
                ANS.append(D[b].pop())
            else:
                ANS.append(A.pop())

        return ANS


A = [2, 7, 11, 15]
B = [1, 10, 4, 11]

S = Solution()
print(S.advantageCount(A, B))
