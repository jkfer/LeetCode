# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# 671


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        if not root:
            return -1

        D = set()

        Q = [root]

        while len(Q) > 0:
            r = Q.pop(0)
            D.add(r.val)
            if r.left:
                Q.append(r.left)

            if r.right:
                Q.append(r.right)

        d = list(D)
        d.sort()
        return d[1] if len(d) > 1 else -1
