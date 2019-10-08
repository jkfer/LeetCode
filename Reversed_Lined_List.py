"""
206.
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# defining a node
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)


def Lprint(node):
    if not node:
        print('No input given')
    
    while node:
        print(node.val, end=" ")
        node = node.next
    print('\n')


class Solution:
    def reverseList(self, head):
        # defining three variables
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        return prev



S = Solution()
Lprint(root)
H = S.reverseList(root)
Lprint(H)

