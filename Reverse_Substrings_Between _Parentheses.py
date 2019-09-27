"""
1190
Reverse Substrings Between Each Pair of Parentheses
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.
"""
import re

class Solution:
    def reverseParentheses(self, s):
        # base case -  replace any empty strings:
        s = re.sub(r"\([^a-z()]*\)", "", s)
        print(s)
        P = r'[a-z]{0,}(\([a-z]*\))[a-z]{0,}'
        patt = re.compile(P)
        while patt.search(s):
            S = patt.search(s)
            repl = S.group(1).strip('()')[::-1]
            s = re.sub(r'\(%s\)' % str(S.group(1)), repl, s)
        
        return s

A = Solution()
x = A.reverseParentheses("uxbpgfzt(cn(nnn()))")
print(x)
