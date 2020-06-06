# https://leetcode.com/problems/interval-list-intersections/
# 986


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26], [99, 100]]


# Referred solutions:
class Solution:
    def intervalIntersection(self, A, B):
        # detect max of lower and min of upper
        i = 0
        j = 0

        ANS = []

        while i < len(A) and j < len(B):
            a_low, a_high = A[i]
            b_low, b_high = B[i]
            if a_low <= b_high and b_low <= a_high:
                ANS.append([max(a_low, b_low), min(a_high, b_high)])

            if a_high <= b_high:
                i += 1
            else:
                j += 1

        return ANS

    def intervalIntersection2(self, A, B):
        # combined = sorted(A + B, key=itemgetter(0))
        combined = sorted(A + B)
        intersection = []
        currentEnd = -1

        for start, end in combined:
            if start <= currentEnd:
                intersection.append([start, min(currentEnd, end)])
            currentEnd = max(currentEnd, end)

        return intersection


S = Solution()
a = S.intervalIntersection2(A, B)
print(a)
