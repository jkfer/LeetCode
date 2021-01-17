# 395
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import Counter


# Referred solution
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n < k:
            return 0
        
        count = Counter(s)
        l = 0
        while l < len(s) and count[s[l]] >= k:
            l += 1
        
        if l == n:
            return l
        
        L1 = self.longestSubstring(s[0:l], k)
        while l < n and count[s[l]] < k:
            l += 1

        if l < n:
            L2 = self.longestSubstring(s[l:], k)
        else:
            L2 = 0

        return max(L1, L2)


s = "aaabb"
k = 3

S = Solution()
print(S.longestSubstring('aaabb', 3))