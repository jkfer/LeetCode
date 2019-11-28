# 1221
# check for count of R and L to be equal in the intersection points


class Solution:
    def check(self, s):
        return s.count("R") == s.count("L")

    def balancedStringSplit(self, s):
        ans = 0
        i = 0
        x = 2
        while i + x <= len(s):
            S = s[:x]
            if self.check(S):
                ans += 1
                s = s[x:]
                x = 2
            else:
                x += 2

        return ans


S = Solution()
print(S.balancedStringSplit("RLRRRLLRLL"))
