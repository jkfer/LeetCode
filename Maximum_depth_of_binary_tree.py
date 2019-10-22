# 104


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = []
        queue.append(root)
        count = 1

        while len(queue) > 0:
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            if len(new_queue) > 0:
                count += 1

            queue = new_queue

        return count


S = Solution()
print(S.maxDepth(root))
