"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # pad the smallest number with 0:
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a
        

        # now both numbers are the same length:
        # add both numbers:
        k = 0
        A = B = 0

        
        for i in reversed(range(len(a))):
            A += int(a[i]) * (2 ** k)
            B += int(b[i]) * (2 ** k)
            k += 1
        
        C = A + B
        
        # convert C to Binary:
        if C == 0:
            return "0"

        ans = ""

        while C > 0:
            rem = C % 2
            C = C // 2

            ans = str(rem) + ans
        
        
        return ans


S = Solution()
x = S.addBinary("0", "0")
print(x)
