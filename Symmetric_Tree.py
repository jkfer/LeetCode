# 101.
# Symmetric Tree
"""
Idea: 
BFS and for each level compare the result and the reverse(result) with each other. 
If they are not equal to each other then return False
else True
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)


class Solution:
    def isSymmetric(self, root):
        # use Queues for BFS:
        if not root:
            return False
        
        if not root.left and not root.right:
            return True
        
        queue = [root]

        while len(queue) > 0 and set(queue) != None:
            level = []
            for _ in range(len(queue)):
                R = queue.pop(0)
                level.append(R.left.val) if R.left else level.append(None)
                level.append(R.right.val) if R.right else level.append(None)

                if R.left:
                    queue.append(R.left)
                if R.right:
                    queue.append(R.right)

            if level != level[::-1]:
                return False

        return True


S = Solution()
print(S.isSymmetric(root))