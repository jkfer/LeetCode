"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

haystack = "aaaaa"
needle = "bba"

class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return -1

        N = len(needle)

        for i in range(len(haystack) - N + 1):
            if haystack[i:i+N] == needle:
                return i

        return -1


S = Solution()
x = S.strStr(haystack, needle)
print(x)