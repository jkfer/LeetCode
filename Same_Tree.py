

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# defining a sample TreeNode:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(None)

root2 = TreeNode(1)
root2.left = TreeNode(None)
root2.right = TreeNode(2)

class Solution:
    def BFS(self, root, res):
            L = []
            R = []
            for ROOT in root:
                if ROOT:
                    res.append(ROOT.val)
                if ROOT.left:
                    L.append(ROOT.left)
                if ROOT.right:
                    R.append(ROOT.right)

            if len(L + R) > 0:
                return self.BFS(L+R, res)
            else:
                return res

    def isSameTree(self, p, q):
        # we will do a bfs search for both trees 
        return True if self.BFS([p], []) == self.BFS([q], []) else False



S = Solution()
x = S.isSameTree(root1, root2)
print(x)

#x1 = S.BFS([root1], [])
#x2 = S.BFS([root2], [])
#print(x1, x2)