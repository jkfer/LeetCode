# https://leetcode.com/problems/path-sum/
# 112

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if root.val == sum:
            if not root.left and not root.right:
                return True
            else:
                return False

        Q = [[root, 0]]

        while Q:
            new_Q = []
            for N, s in Q:
                if not N.left and not N.right:
                    if s + N.val == sum:
                        return True
                if N.left:
                    new_Q.append([N.left, N.val + s])
                if N.right:
                    new_Q.append([N.right, N.val + s])
            Q = new_Q

        return False
