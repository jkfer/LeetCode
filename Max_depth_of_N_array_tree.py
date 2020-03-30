# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# 559


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        if not root.children:
            return 1

        depth = 0
        Q = [root]

        while len(Q) > 0:
            depth += 1
            newQ = []
            for n in Q:
                if n:
                    newQ += n.children
            Q = newQ

        return depth
