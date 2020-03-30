# https://leetcode.com/problems/leaf-similar-trees/
# 872


import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getLeaf(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        Q = [root]
        ans = []
        last = False

        while not last:
            last = True
            newQ = []
            for n in Q:
                if n.left or n.right:
                    last = False
                    if n.left:
                        newQ.append(n.left)

                    if n.right:
                        newQ.append(n.right)
                else:
                    newQ.append(n)
            Q = newQ

        return [n.val for n in Q]

    def leafSimilar(self, root1, root2):
        return self.getLeaf(root1) == self.getLeaf(root2)
