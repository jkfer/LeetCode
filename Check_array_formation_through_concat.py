# https://leetcode.com/problems/check-array-formation-through-concatenation/


class Solution:
    def canFormArray(self, arr, pieces):
        D = dict()
        for x in pieces:
            D[x[0]] = x
        
        # print(D)
        ans = []
        for a in arr:
            if a in D:
                ans += D[a]
        
        return ans == arr   


arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
S = Solution()
print(S.canFormArray(arr, pieces))