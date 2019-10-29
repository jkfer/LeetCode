# 680

"""
Tough.
Idea:
compare charachters in both ends (first and last).
If they are equal to each other remove both. and repeat.
If they are not equal to each other:
    - include the first if the string[:-1] is a plaindrome
    - include the last if the string[1:] is a plaindrome

"""


class Solution:
    def checkplain(self, s):
        st = 0
        end = len(s) - 1
        while st <= end:
            if s[st] != s[end]:
                return False
            st += 1
            end -= 1
        return True

    def validPalindrome(self, s):
        if len(s) <= 2:
            return True

        while len(s) > 0:
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                if self.checkplain(s[:-1]):
                    s = s[:-1]
                elif self.checkplain(s[1:]):
                    s = s[1:]
                else:
                    return False

        return True


S = Solution()
print(S.validPalindrome("aba"))
print(S.checkplain("5b75"))
