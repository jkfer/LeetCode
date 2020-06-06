# https://leetcode.com/problems/merge-intervals/
# 56

A = [[1, 3], [2, 6], [8, 10], [15, 18]]
B = [[1, 4], [4, 5]]
C = [[1, 4], [5, 6]]
D = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
# [[1,6],[8,10],[15,18]]


class Solution:
    def merge(self, intervals):
        ANS = []
        currentMax = -1

        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals)
        print(intervals)
        curr_min, curr_max = intervals[0]
        i = 1
        ANS = [[curr_min, curr_max]]

        while i < len(intervals):
            a, b = intervals[i]
            if a <= curr_max:
                ANS.pop()
                ANS.append([min(a, curr_min), max(b, curr_max)])
                curr_min = min(a, curr_min)
                curr_max = max(b, curr_max)
            else:
                ANS.append([a, b])
                curr_min = a
                curr_max = b

            i += 1
            # print(ANS, curr_min, curr_max)

        return ANS


S = Solution()
ans = S.merge(D)
print(ans)
