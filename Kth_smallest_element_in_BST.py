# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230
# Medium - Passed

"""
Idea:
In-order traversal of a BST gives a non decreasing array
if you store all the values in a list. once you get to the kth value,
just break the loop.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rtraverse(self, root):
        s = []
        while root:
            s.append(root)
            root = root.left
        return s

    def kthSmallest(self, root, k):
        # get the left nodes:
        stack = self.rtraverse(root)
        count = 0

        while len(stack) > 0:
            N = stack.pop()

            ANS.append(N.val)
            count += 1

            if N.right:
                stack += self.rtraverse(N.right)

            if count == k:
                break

        return ANS[-1]
