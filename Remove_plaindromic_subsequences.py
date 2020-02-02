# https://leetcode.com/contest/weekly-contest-173/problems/remove-palindromic-subsequences/
# 1332
# Idea here is that, if there is only two alphabets in a string
# you can delete all of the one chars from the string,
# and then all of the the other chars from the string
# as each charachter counts as a plaindrome


class Solution:
    def removePalindromeSub(self, s):
        if s == "":
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2


S = Solution()
print(S.removePalindromeSub('baabb'))
