# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# 1315
# Medium - Passed


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def return grand parent val of a given node:
    def evenR(self, root):
        S = 0
        Q = [root.left, root.right]
        for n in Q:
            if n:
                if n.left:
                    S += n.left.val

                if n.right:
                    S += n.right.val
        return S

    def sumEvenGrandparent(self, root):
        if not root:
            return 0

        # BFS through the tree with identifying the
        Q = [root]
        S = 0

        while len(Q) > 0:
            R = Q.pop(0)

            if R.val % 2 == 0:
                S += self.evenR(R)

            if R.left:
                Q.append(R.left)

            if R.right:
                Q.append(R.right)
        return S
