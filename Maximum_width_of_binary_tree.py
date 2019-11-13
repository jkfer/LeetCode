# 662
# Medium


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


class Solution:
    def widthOfBinaryTree(self, root):
        # base:
        if not root:
            return 0

        # BFS search and at each width save the length:
        queue = [root]
        m = len(queue)

        while len(queue) > 0:
            new_queue = []

            for R in queue:
                new_queue.append(R.left if R else None)
                new_queue.append(R.right if R else None)

            i = 0
            j = len(new_queue)

            for i in range(j):
                if new_queue[i]:
                    break

            if new_queue[i] is None:
                break

            for j in range(j-1, -1, -1):
                if new_queue[j]:
                    break

            m = max(m, j-i+1)
            queue = new_queue

        return m


S = Solution()
print(S.widthOfBinaryTree(root))
