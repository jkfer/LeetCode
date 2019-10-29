# 344


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        st = 0
        en = len(s) - 1

        while st <= en:
            a, b = s[st], s[en]
            s[st] = b
            s[en] = a

            st += 1
            en -= 1

        # print(s)


S = Solution()
S.reverseString(list('hello'))
