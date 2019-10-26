# 876
# Middle of the Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        if not head.next:
            return head

        curr = head
        L = []
        
        while head:
            L.append(head)
            head = head.next
        
        return L[len(L) // 2]

