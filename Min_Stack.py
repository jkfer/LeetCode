# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)


S = MinStack()
S.push(1)
S.push(2)
print(S.getMin())
