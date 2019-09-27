"""
1189
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

class Solution:
    def maxNumberOfBalloons(self, text):
        res = []
        for L in 'balon':
            i = list(text).count(L)
            if L == 'l' or L == 'o':
                res.append(i / 2)
            else:
                res.append(i)
        
        return min(res)
