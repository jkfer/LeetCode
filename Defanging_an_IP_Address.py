"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

import re

class Solution:
    def defangIPaddr(self, address):
        add = re.sub('\.', '[.]', address)
        return add

S = Solution()
x = S.defangIPaddr("255.100.50.0")
print(x)