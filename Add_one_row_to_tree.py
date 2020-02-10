# https://leetcode.com/problems/add-one-row-to-tree/
# 623
# Medium -- Passed


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


R = TreeNode(4)
R.left = TreeNode(2)
R.right = TreeNode(6)
R.left.left = TreeNode(3)
R.left.right = TreeNode(1)
R.right.left = TreeNode(5)


class Solution:
    # print tree for visualization
    def Treep(self, head):
        S = [head]
        while len(S) > 0 and set(S) != {None}:
            ANS = []
            new_s = []
            for r in S:
                if r:
                    ANS.append(r.val)
                    new_s.append(r.left) if r.left else new_s.append(None)
                    new_s.append(r.right) if r.right else new_s.append(None)
                else:
                    ANS.append(None)
            print(ANS)
            S = new_s

    def addOneRow(self, root, v, d):
        ref = root
        S = [root]
        D = 1
        prev = []

        # Base case - if d == 1
        if d == 1:
            r = TreeNode(v)
            r.left = root
            return r

        while len(S) > 0 and set(S) != {None}:
            prev = S
            nex = []
            for r in S:
                if r:
                    nex.append(r.left) if r.left else nex.append(None)
                    nex.append(r.right) if r.right else nex.append(None)

            D += 1
            if D == d:
                # print(prev)
                # print(nex)
                for n in prev:
                    if n:
                        if not n.left and not n.right:
                            n.left = TreeNode(v)
                            n.right = TreeNode(v)
                        else:
                            if n.left or n.right:
                                if n.left:
                                    rl = n.left
                                    n.left = TreeNode(v)
                                    n.left.left = rl
                                else:
                                    n.left = TreeNode(v)

                                if n.right:
                                    rr = n.right
                                    n.right = TreeNode(v)
                                    n.right.right = rr
                                else:
                                    n.right = TreeNode(v)

            S = nex
        return ref


S = Solution()
R = S.addOneRow(R, 1, 2)
S.Treep(R)
