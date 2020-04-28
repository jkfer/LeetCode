# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299/
#


class Solution:
    def stringShift(self,  s,  shift):
        if len(s) <= 1:
            return s

        fshift = 0
        for a, b in shift:
            if a == 0:
                fshift -= b
            else:
                fshift += b

        print(fshift)
        if fshift == 0 or fshift % len(s) == 0:
            return s

        # reset fshift:
        if fshift > 0:
            fshift %= len(s)
            for i in range(fshift):
                s = s[-1] + s[:-1]
        else:
            fshift *= -1
            fshift %= len(s)
            for i in range(fshift):
                s = s[1:] + s[0]

        print(s)


s = "mecsk"
shift = [[1, 4], [0, 5], [0, 4], [1, 1], [0, 5]]
S = Solution()
S.stringShift(s,  shift)
