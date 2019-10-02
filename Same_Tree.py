

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# defining a sample TreeNode:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(4)

class Solution:
    def isSameTree(self, p, q):
        # we will do a bfs search for both trees 
        def BFS(root, res=[]):
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
                BFS(L+R, res)
            else:
                return res

        return BFS(p) == BFS(q)

S = Solution()
ans = S.isSameTree([root], [root2])
print(ans)