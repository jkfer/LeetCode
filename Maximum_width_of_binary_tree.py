# 662
# Medium
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.right = TreeNode(1)
root.left.left.left = TreeNode(1)
root.right.right.right = TreeNode(1)


# Referred solution:
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 0)] if root else [])
        max_width = 0
        while queue:
            width = queue[-1][1]-queue[0][1]+1
            max_width = max(max_width, width)
            for _ in range(len(queue)):
                node, val = queue.popleft()
                if node.left:
                    queue.append((node.left, val*2+1))
                if node.right:
                    queue.append((node.right, val*2+2))
        return max_width

    def widthOfBinaryTree(self, root):
        if root is None:
            return 0

        l1, l2 = [root], []
        end = root
        res = 1
        while len(l1) > 0:
            for node in l1:
                l2.append(node.left if node else None)
                l2.append(node.right if node else None)

            ln = len(l2)
            for i in range(len(l2)):
                if l2[i]:
                    break

            if i == ln:
                break

            for j in range(ln-1, -1, -1):
                if l2[j]:
                    break

            res = max(res, j - i + 1)

            l1 = l2[i:j+1].copy()
            l2 = []

        return res


S = Solution()
print(S.widthOfBinaryTree(root))
