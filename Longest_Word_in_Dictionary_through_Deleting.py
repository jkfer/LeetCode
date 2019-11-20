# 524
# Medium

"""
This will be simple to do when we use regular expressions.
edit: regular expressions solution times out for larger solutions.
"""

import re


class Solution:
    # solution times out for larger inputs
    def findLongestWord(self, s, d):
        dd = list(set(d))
        dd.sort()
        ans = ""
        for w in d:
            patt = ".*".join(w)
            if re.search(patt, s):
                if len(w) > len(ans):
                    ans = w
                elif len(w) == len(ans):
                    x = [w, ans]
                    x.sort()
                    ans = x[0]
        return ans

    # Accepted solution:
    def findLongestWord2(self, s, d):
        # we will create a logic to find if a substring matches s
        # then use that logic while iterating through d
        def match(A, substr):
            i = j = 0
            while i < len(A) and j < len(substr):
                if A[i] == substr[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j < len(substr):
                return False
            else:
                return True

        ans = ""
        for word in d:
            if match(s, word):
                if ans == "":
                    ans = word
                else:
                    if len(ans) == len(word):
                        x = [ans, word]
                        x.sort()
                        ans = x[0]
                    elif len(ans) < len(word):
                        ans = word
        return ans


S = Solution()
print(S.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))

print(S.findLongestWord2("abpcplea", ["ale", "apple", "monkey", "plea"]))
