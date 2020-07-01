# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# MEDIUM
# 1448


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        C = 1
        Q = [[root, root.val]]
        while len(Q) > 0:
            node, v = Q.pop(0)
            if node.left:
                if node.left.val >= v:
                    Q.append([node.left, node.left.val])
                    C += 1
                else:
                    Q.append([node.left, v])

            if node.right:
                if node.right.val >= v:
                    Q.append([node.right, node.right.val])
                    C += 1
                else:
                    Q.append([node.right, v])

        return C
