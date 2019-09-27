"""
You need to find the largest value in each row of a binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

class Solution:
    

    def largestValues(self, root):
        result = []
        ROOT = [root]
    
        def eval(root):
            result.append(max(root))

    
        def traverse(ROOT):
            values = []
            next_ROOT = []

            for root in ROOT:
                if root:
                    values.append(root.val)
                    next_ROOT.append(root.left)
                    next_ROOT.append(root.right)
            
            eval(values)
            if any(i != None for i in next_ROOT):
                traverse(next_ROOT)
            else:
                return

        if root:
            traverse(ROOT)

        return result


S = Solution()
x = S.largestValues(root)
print(x)