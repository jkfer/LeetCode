# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Referred solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        length = l = 0
        
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = max(length, r - l + 1)
        
        return length