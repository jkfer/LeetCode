# 19
"""
Idea:
provided node is N
find the nth node from the start of N. Say this is X
from there:
    = traverse N and X simultaneously until X.next is none.
    = now you have reached the node where the next node will be the nth from the last.
from here its simply removing the next node of N task
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)


class Solution:
    def Nprint(self, root):
        while root:
            print(root.val),
            root = root.next


    def removeNthFromEnd(self, head, n):
        head_ref = head
        # find the nth:
        other = head
        count = 0

        while count < n:
            other = other.next
            count += 1

        if not other:
            # if you get here that means n = length of the node.
            # hence you have to remove the first node only:
            return head_ref.next

        while other.next != None:
            other = other.next
            head = head.next

        second = head.next.next
        head.next = second

        return head_ref


S = Solution()
k = S.removeNthFromEnd(root, 4)
S.Nprint(k)

