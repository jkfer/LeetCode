# https://leetcode.com/problems/camelcase-matching/
# 1023
# Medium - Passed


import re


class Solution:
    def camelMatch(self, queries, pattern):
        # Create the pattern for re:
        i = 0
        new_patt = "(.*)"
        while i < len(pattern):
            new_patt += pattern[i] + "(.*)"
            i += 1

        # print(new_patt)

        ANS = [True] * len(queries)

        for i, q in enumerate(queries):
            # Capture the charachters to inspect
            S = re.search(new_patt, q)

            if not S:
                ANS[i] = False
            else:
                # print(S.groups())
                for s in "".join(S.groups()):
                    if s.isupper():
                        ANS[i] = False
                        break

        return ANS


queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"]
pattern = "CooP"

S = Solution()
print(S.camelMatch(queries, pattern))
