# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 235
"""
given tree is a BST
in BST for any node that contains left and right nodes -
node.left.val < node.val < node.right.val

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# referred solution
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ref = root

        pval = p.val
        qval = q.val

        while root:
            parent_val = root.val

            if pval > parent_val and qval > parent_val:
                node = node.right
            elif pval < parent_val and qval < parent_val:
                node = node.left
            else:
                return node





