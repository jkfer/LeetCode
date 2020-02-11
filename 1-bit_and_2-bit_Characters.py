# https://leetcode.com/problems/1-bit-and-2-bit-characters/
# 717


class Solution:
    def isOneBitCharacter(self, bits):
        last = False
        i = 0

        while i < len(bits):
            if bits[i] == 1 and i+1 < len(bits):
                last = False
                i += 2
            else:
                last = True
                i += 1

        return last


bits = [1, 0, 0]
S = Solution()
print(S.isOneBitCharacter(bits))
