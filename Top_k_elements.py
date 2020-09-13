# https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter
import heapq


# Referred solution:
class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


N = [3, 0, 1, 0]
S = Solution()
ans = S.topKFrequent(N, 2)
print(ans)
