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

        while P == Q and len(queue_P) == len(queue_Q) and \
                set(queue_Q) != {None} and set(queue_Q) != {None}:
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

    def isSameTree2(self, p, q):
        if (p and not q) or (q and not p):
            return False

        P = [p]
        Q = [q]

        while len(P) > 0 and len(Q) > 0:
            p, q = P.pop(0), Q.pop(0)
            if p and q:
                if p.val != q.val:
                    return False

                if p.left:
                    P.append(p.left)
                else:
                    P.append(None)

                if p.right:
                    P.append(p.right)
                else:
                    P.append(None)

                if q.left:
                    Q.append(q.left)
                else:
                    Q.qppend(None)

                if q.right:
                    Q.append(q.right)
                else:
                    Q.append(None)
            else:
                if (p and not q) or (q and not p):
                    return False

        return True

    # referred solution - using recurtion
    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right)
        if not p and not q:
            return True
        return False
