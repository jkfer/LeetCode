# 107
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


"""
Recalling:
BFS - queue
DFS (3 types) - stack
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        ans = []
        Q = [root]
        level = []

        while len(Q) > 0:
            level = []
            a = []
            for n in Q:
                a.append(n.val)
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            ans.append(a)
            Q = level

        return ans[::-1]
