"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def deleteDuplicates(self, head):
        start = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return start


    def printL(self, head):
        while head:
            print(head.val),
            head = head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
#head.next.next.next = ListNode(3)
#head.next.next.next.next = ListNode(3)


S = Solution()
S.printL(head)
print('\n')
H = S.deleteDuplicates(head)
S.printL(head)
