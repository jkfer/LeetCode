"""
1200

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6


Ex:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""


class Solution:
    ## **** Good solution but time complexity is high as list is iterated twice
    def minimumAbsDifference(self, arr):
        arr.sort()
        # base case - if len(arr) == 2:
        if len(arr) == 2:
            return [arr]
        
        # find the min abs diff
        diff = abs(min(arr)-max(arr))

        # iterate throught the list to find the min abs diff:
        for i in range(len(arr)-1):
            D = abs(arr[i] - arr[i+1])
            if D < diff:
                diff = D

        # now iterate through the array to find the pairs
        res = []
        for i in range(len(arr)-1):
            DD = arr[i] + diff
            if DD in arr[i+1:]:
                res.append([arr[i], DD])

        return res

    # better and successful solution
    def minimumAbsDifference2(self, arr):
        arr.sort()
        # base case - if len(arr) == 2:
        if len(arr) == 2:
            return [arr]

        # define a dict - D[diff] = []
        D = {}
        for i in range(len(arr) - 1):
            d = abs(arr[i+1] - arr[i])
            if d in D:
                D[d].append([arr[i],arr[i+1]])
            else:
                D[d] = [[arr[i],arr[i+1]]]
        
        return D[min(D.keys())]


S = Solution()
x = S.minimumAbsDifference2([3,8,-10,23,19,-4,-14,27])
print(x)
        