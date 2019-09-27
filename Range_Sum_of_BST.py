"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Define a TreeNode - Traversal: Preorder
# [10,5,15,3,7,null,18]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
#root.right.left = TreeNode(Null
root.right.right = TreeNode(18)

class Solution:
    count = 0
    
    def rangeSumBST(self, root, L, R):
        def eval(root):
            if L <= root.val <= R:
                self.count += root.val

        def traverse_node(root):
            if root:
                eval(root)
        
            if root.left:
                traverse_node(root.left)
            
            if root.right:
                traverse_node(root.right)

        traverse_node(root)
        return self.count




"""
class Solution:
    count = 0
    
    def rangeSumBST(self, root, L, R):
        def eval_node(root):
            if L <= root.val <= R:
                self.count += root.val

        def traverse_node(root):
            if root:
                eval_node(root)
            if root.left:
                traverse_node(root.left)
            if root.right:
                traverse_node(root.right)

        traverse_node(root)
        return self.count
"""



#S = Solution()
#S.preOrder(root)
S = Solution()
x = S.rangeSumBST(root, 7, 15)
print(x)