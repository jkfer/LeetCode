# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si = 0
        ti = 0

        while ti < len(t) and si < len(s):
            if t[ti] == s[si]:
                ti += 1
                si += 1
            else:
                ti += 1

        return si == len(s)
