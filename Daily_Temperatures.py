# https://leetcode.com/problems/daily-temperatures/
# 739


class Solution:
    def dailyTemperatures(self, T):
        ANS = [0] * len(T)
        stack = []
        for i, p in enumerate(T):
            while stack and stack[-1][1] < p:
                j, v = stack.pop()
                ANS[j] = i - j
            stack.append([i, p])

        return ANS


T = [73, 74, 75, 71, 69, 72, 76, 73]
S = Solution()
print(S.dailyTemperatures(T))
