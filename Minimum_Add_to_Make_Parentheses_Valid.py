# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# 921
# Medium - passed


class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        for b in S:
            if not stack or b == "(":
                stack.append(b)
            elif b == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(b)

        return len(stack)


S = Solution()
ans = S.minAddToMakeValid("()))((")
print(ans)
