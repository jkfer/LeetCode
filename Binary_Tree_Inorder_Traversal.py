# 94
# Inorder - Left, Root, Right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


class Solution:
    # going with an iterative solution:
    # obviously stack is the way
    def inorderTraversal(self, root):
        def ino(root):
            s = []
            while root is not None:
                s.append(root)
                root = root.left
            return s

        ANS = []
        stack = ino(root)

        while len(stack) > 0:
            R = stack.pop()
            ANS.append(R.val)
            if R.right:
                stack += ino(R.right)

        return ANS


S = Solution()
print(S.inorderTraversal(root))
