# https://leetcode.com/problems/univalued-binary-tree/
# 965

"""
Idea: You can do a BFS and ensure that all values are the same.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        Q = [root]
        V = []

        while len(Q) > 0:
            R = Q.pop(0)
            if (V == []) or (V[-1] == R.val):
                V.append(R.val)
                if R.left:
                    Q.append(R.left)
                if R.right:
                    Q.append(R.right)
            else:
                return False

        return True
