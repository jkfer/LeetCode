"""
Given a set of non-negative integers (consider them unique with no duplicates), and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input:  set = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9
"""

# set - the set
# n - number of elements in the set
# the target sum

# recursive
def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    elif n == 0 and sum != 0:
        return False

    if set[n-1] > sum:
        return isSubsetSum(set, n-1, sum)
    else:
        return isSubsetSum(set, n-1, sum-set[n-1])


set = list(set([3, 34, 4, 12, 5, 2]))
sum = 9
n = len(set)

print(isSubsetSum(set, n, sum))