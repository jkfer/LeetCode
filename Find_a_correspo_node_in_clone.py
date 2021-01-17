# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        Q = [cloned]
        while len(Q) > 0:
            R = Q.pop(0)
            if R.val == target.val:
                return R
            
            if R.left:
                Q.append(R.left)
            
            if R.right:
                Q.append(R.right)