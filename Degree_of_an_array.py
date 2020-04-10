# https://leetcode.com/problems/degree-of-an-array/
# 697


import collections


class Solution:
    def findShortestSubArray(self, nums):
        # Count the number of items in nums
        D = dict()
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1

        ans = []
        index = []

        for a, b in D.items():
            if b == max(D.values()):
                index.append(a)

        for ll in index:
            st = 0
            en = len(nums) - 1
            while nums[st] != ll:
                st += 1
            while nums[en] != ll:
                en -= 1
            ans.append(en-st+1)

        return min(ans)

    # refferred solutions:
    def findShortestSubArray2(self, nums):
        """
        Idea here is to use the indexes to save positions of each values
        Then you can compute the distance to include all of the values
        then find the smallest distance
        """
        D = collections.defaultdict(list)
        Dl = collections.defaultdict(int)

        for i, n in enumerate(nums):
            D[n].append(i)
            Dl[n] += 1

        ans = []
        m = max(Dl.values())
        for ll in D.values():
            if len(ll) == m:
                ans.append(max(ll) - min(ll) + 1)

        return min(ans)


S = Solution()
print(S.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
