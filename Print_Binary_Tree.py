# 655
# https://leetcode.com/problems/print-binary-tree/
# Medium - tough

"""
Works only for the examples provided. Needs work.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(5)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)


class Solution:
    def printTree(self, root):
        ans = []
        R = [root]

        while len(R) > 0:
            a = []
            level = []
            for n in R:
                if n:
                    a.append(str(n.val))
                    if n.left:
                        level.append(n.left)
                    else:
                        level.append(None)

                    if n.right:
                        level.append(n.right)
                    else:
                        level.append(None)
                else:
                    a.append("")

            if set(a) != {""}:
                ans.append(a)

            R = level

        # get the height and width of the tree for output
        width = (2 ** len(ans)) - 1
        height = len(ans)

        # create the matrix:
        matrix = [["" for i in range(width)] for j in range(height)]

        # print(ans)
        # print(matrix)
        # print(height, width)

        for l in range(height):
            i = width // 2
            save = i
            for val in ans[l]:
                matrix[l][i] = val
                i += 2 ** height
            width = save
            height -= 1

        print(matrix)


# This is a copied over solution. Not original
class Solution2:
    # find the height of the tree
    def height(self, root):
        if not root:
            return 0
        h = 1 + max(self.height(root.left), self.height(root.right))
        return h

    def printTree(self, root):
        if not root:
            return None

        h = self.height(root)

        row = h
        col = 0
        for i in range(h):
            col += pow(2, i)

        rlt = [[""] * col for _ in range(row)]

        st = [(root, 0, col-1)]
        new_st = []
        lvl = 0
        while st:
            node, l, h = st.pop(0)
            mid = int((l+h)/2)
            rlt[lvl][mid] = str(node.val)
            if node.left:
                new_st.append((node.left, l, mid))
            if node.right:
                new_st.append((node.right, mid+1, h))
            if not st:
                lvl += 1
                st = new_st
                new_st = []

        return rlt


S = Solution2()
print(S.printTree(root2))
