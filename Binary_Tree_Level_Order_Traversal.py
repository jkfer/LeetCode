"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        res = []
        
        def traverse(node):
            R = []
            next = []
            for n in node:
                if n:
                    R.append(n.val)
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)
            
            res.append(R)
            
            if len(next) == 0:
                return res
            else:
                return traverse(next)
            
                    
        if root:            
            return traverse([root])
        else:
            return []


if __name__ == "__main__":
    # Ex:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    S = Solution()
    x = S.levelOrder(root)
    print(x)


