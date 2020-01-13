# https://leetcode.com/problems/deepest-leaves-sum/
# 1302
# Medium Trees - passed


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root):
        # BFS
        # Last nodes will not have root.left or root right
        Q = [root]
        newQ = []
        last = []
        while len(Q) > 0:
            R = Q.pop(0)
            last.append(R.val)

            if R.left:
                newQ.append(R.left)

            if R.right:
                newQ.append(R.right)

            if not Q:
                if len(newQ) > 0:
                    Q = newQ
                    newQ = []
                    last = []

        return sum(last)
