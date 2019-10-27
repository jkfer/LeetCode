# 563


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   ANS =


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


class Solution:
    ans = 0

    def findTilt(self, root):
        def tilt(root):
            if not root:
                return 0
            left, right = tilt(root.left), tilt(root.right)
            self.ans += abs(left-right)
            return root.val + left + right

        tilt(root)
        return self.ans


S = Solution()
print(S.findTilt(root))
