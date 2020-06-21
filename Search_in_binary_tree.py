# https://leetcode.com/problems/search-in-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        if not root:
            return None

        while root:
            if root.val == val:
                return root
            else:
                if val > root.val:
                    root = root.right
                else:
                    root = root.left

        return None
