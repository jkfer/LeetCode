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
        1000: "M", 
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM"
    }

    def intToRoman(self, num):
        ans = []
        while num > 0:
            x = len(str(num)) - 1
            y = int(str(num)[0])
            
            nu = y * int(pow(10, x))
            if nu in self.D:
                ans.append(self.D[nu])
            else:
                if y in [6, 7, 8]:
                    small_ans = self.D[5*int(pow(10, x))] + self.D[int(pow(10, x))] * (y-5)
                    ans.append(small_ans)
                else:
                    ans.append(self.D[int(pow(10, x))] * y)
            
            num -= nu
        
        print "".join(ans)



S = Solution()
S.intToRoman(199)
