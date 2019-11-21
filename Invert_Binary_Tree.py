# 226

# This should be easy just do the BFS with root, right and left order,
# instead of the traditional root, left and right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


class Solution:
    def Tprint(self, root):
        if not root:
            return root

        q = [root]
        while len(q) > 0:
            n = q.pop(0)
            print(n.val, end=",")
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print("\n")

    def invertTree(self, root):
        if not root:
            return root

        ref = root
        Q = [root]

        while len(Q) > 0:
            N = Q.pop(0)
            L = N.left
            R = N.right

            N.left = R
            N.right = L

            if N.left:
                Q.append(N.left)
            if N.right:
                Q.append(N.right)

        return ref


S = Solution()
S.Tprint(root)
# print("\n")
R = S.invertTree(root)
S.Tprint(R)
