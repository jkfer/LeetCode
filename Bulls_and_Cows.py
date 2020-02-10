# https://leetcode.com/problems/bulls-and-cows/
# 299


import collections


class Solution:
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0

        secret_other = collections.defaultdict(int)
        guess_other = collections.defaultdict(int)

        for s, g in zip(secret, guess):
            # if s == g we can add count to bulls
            if s == g:
                bulls += 1
            else:
                secret_other[s] += 1
                guess_other[g] += 1

        # cows
        for k in secret_other:
            cows += min(secret_other[k], guess_other[k])

        return "%sA%sB" % (str(bulls), str(cows))


secret = "1807"
guess = "7810"

S = Solution()
print(S.getHint(secret, guess))
