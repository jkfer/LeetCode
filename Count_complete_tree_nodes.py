# https://leetcode.com/problems/count-complete-tree-nodes/
# 222
# Medium


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        Q = [root]
        c = 0

        while len(Q) > 0:
            newQ = []
            for n in Q:
                c += 1
                if n.left:
                    newQ.append(n.left)
                if n.right:
                    newQ.append(n.right)
            Q = newQ

        return c
