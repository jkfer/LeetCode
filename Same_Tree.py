# 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if (p and not q) or (q and not p):
            return False

        P = []
        Q = []

        # BFS:
        queue_P = [p]
        queue_Q = [q]

        while P == Q and len(queue_P) == len(queue_Q) and set(queue_Q) != {None} and set(queue_Q) != {None}:
            p = queue_P.pop(0)
            q = queue_Q.pop(0)
            if p:
                P.append(p.val)
                queue_P.append(p.left)
                queue_P.append(p.right)

            if q:
                Q.append(q.val)
                queue_Q.append(q.left)
                queue_Q.append(q.right)

            if P != Q:
                return False

        return True
