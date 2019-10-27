# 12

from math import pow


class Solution:
    D = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    def intToRoman(self, num):
        ans = []
        for i, a in enumerate(str(num)[::-1]):
            ans.append(int(a) * int(pow(10, i)))
        print(ans[::-1])


S = Solution()
S.intToRoman(567)
