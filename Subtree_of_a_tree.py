"""
572:

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Idea: convert the input TreeNode to a string and then compare them.
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def traverse(self, root):
        if root:
            return ","+"%s"%str(root.val)+","+"%s"%self.traverse(root.left)+","+"%s"%self.traverse(root.right)+","
        return None


    def isSubtree(self, s, t):
        S = self.traverse(s)
        T = self.traverse(t)
        #print(S, T)
        if S.find(T) >= 0:
            return True
        else:
            return False



root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(5)


S = Solution()
x = S.isSubtree(root1, root2)
print(x)