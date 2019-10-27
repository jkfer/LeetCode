# 144
# Preorder Trav - Root, Left, Right
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


class Solution:
    def preorderTraversal(self, root):
        # going with the iterative solution type for this:
        if not root:
            return

        ANS = []
        stack = [root]

        while len(stack) > 0:
            R = stack.pop()
            ANS.append(R.val)
            if R.right:
                stack.append(R.right)
            if R.left:
                stack.append(R.left)

        return ANS


S = Solution()
print(S.preorderTraversal(root))
