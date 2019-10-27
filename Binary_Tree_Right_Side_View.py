# 199
# Binary Tree Right Side View

"""
Idea: 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
#root.left = TreeNode(2)
root.right = TreeNode(2)
#root.left.right = TreeNode(5)
#root.right.right = TreeNode(4)


class Solution:
    def rightSideView(self, root):
        # base:
        if not root:
            return []
        
        queue = [root]
        ANS = []

        while len(queue) > 0:
            ANS.append(queue[-1].val)
            new_queue = []
            for R in queue:
                if R.left:
                    new_queue.append(R.left)
                if R.right:
                    new_queue.append(R.right)
            queue = new_queue
        
        return ANS


S = Solution()
print(S.rightSideView(root))