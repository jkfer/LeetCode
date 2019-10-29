# 654


"""
What is a maximum binary tree?
A maximum tree building on this array is defined as follow: The root is the big number in the array. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number

Idea:
have a function to take in an array and give node, L and R for L and R using recursion
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def consTree(self, arr):
        if len(arr) == 0:
            return None

        i = arr.index(max(arr))
        L = arr[:i]
        R = arr[i+1:]

        node = TreeNode(arr[i])
        node.left = self.consTree(L)
        node.right = self.consTree(R)

        return node

    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        T = self.consTree(nums)
        return T
