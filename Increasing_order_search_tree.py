# https://leetcode.com/problems/increasing-order-search-tree/
# 897


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root):
        S = []
        while root:
            S.append(root)
            root = root.left
        return S

    def increasingBST(self, root):
        stack = self.helper(root)
        ans = []

        while len(stack) > 0:
            v = stack.pop()

            if v.right:
                stack += self.helper(v.right)

            v.left = v.right = None
            ans.append(v)

        for i in range(len(ans) - 1):
            ans[i].right = ans[i+1]

        return ans[0]
