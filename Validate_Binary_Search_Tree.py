# 98
"""
inorder => left, root, right.
for BST the inorder should be strictly incremental.
So inorder traverse a node
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(7)


class Solution:
    def T(self, root):
        a = []
        if not root:
            return a

        while root:
            a.append(root)
            root = root.left

        return a

    # Test case fails with recursive approach
    def traverse(self, root, ans=[]):
        if root:
            self.traverse(root.left, ans)
            ans.append(root.val)
            self.traverse(root.right, ans)

        return ans

    # Using recursive solution -- fails
    def isValidBST0(self, root):
        if not root:
            return True

        L = self.traverse(root)
        if len(L) == 1:
            return True

        for i in range(1, len(L)):
            if L[i-1] >= L[i]:
                return False

        return True

    # pass
    def isValidBST(self, root):
        if not root:
            return True

        ans = []
        L = self.T(root)
        while len(L) > 0:
            p = L.pop()
            ans.append(p.val)

            if p.right:
                L += self.T(p.right)

        for i in range(1, len(ans)):
            if ans[i-1] >= ans[i]:
                return False

        return True


S = Solution()
print(S.isValidBST(root))
