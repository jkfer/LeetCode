# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# 1305
# Medium
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1, root2):
        # create a dict:
        D = collections.defaultdict(int)
        Q1 = [root1]
        Q2 = [root2]

        if root1:
            while len(Q1) > 0:
                newQ1 = []
                for n1 in Q1:
                    D[n1.val] += 1
                    if n1.left:
                        newQ1.append(n1.left)
                    if n1.right:
                        newQ1.append(n1.right)
                Q1 = newQ1

        if root2:
            while len(Q2) > 0:
                newQ2 = []
                for n2 in Q2:
                    D[n2.val] += 1
                    if n2.left:
                        newQ2.append(n2.left)
                    if n2.right:
                        newQ2.append(n2.right)
                Q2 = newQ2

        ANS = []
        E = list(D.keys())
        E.sort()
        for v in E:
            ANS += [v] * D[v]

        return ANS

    # Better solution
    def bfs(self, root):
        if not root:
            return []

        D = collections.deque()
        D.append(root)
        V = []

        while len(D) > 0:
            d = D.popleft()
            V.append(d.val)

            if d.left:
                D.append(d.left)
            if d.right:
                D.append(d.right)

        return V

    def getAllElements2(self, root1, root2):
        return sorted(self.bfs(root1) + self.bfs(root2))
