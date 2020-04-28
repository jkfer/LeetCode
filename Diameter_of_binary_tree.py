# https://leetcode.com/problems/diameter-of-binary-tree/
# 543


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tdepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        d = 0
        stack = [root]
        while len(stack) > 0:
            d += 1
            new_stack = []
            for n in stack:
                if n.left:
                    new_stack.append(n.left)
                if n.right:
                    new_stack.append(n.right)
            stack = new_stack

        return d

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        # bfs
        m = 0
        stack = [root]
        while len(stack) > 0:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
                m = max(m, self.tdepth(node.left) + self.tdepth(node.right))
            stack = new_stack
        return m
