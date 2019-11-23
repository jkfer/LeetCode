# 617

# Go layer by layer at BFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# referred solution for this. Need focus on recursion concepts.
class Solution:
    def mergeTrees(self, n1, n2):
        if n1 and n2:
            root = TreeNode(n1.val + n2.val)
            root.left = self.mergeTrees(n1.left, n2.left)
            root.right = self.mergeTrees(n1.right, n2.right)
            return root
        else:
            return n1 if n1 else n2

    # Alternative - better written.
    def mergeTrees2(self, t1, t2):
        if not t1 and not t2:
            return

        if not t1:
            res = t2
        elif not t2:
            res = t1
        else:
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)
            res.right = self.mergeTrees(t1.right, t2.right)

        return res
