"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# defining a node:
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(3)


class Solution:
    def printL(self, head):
        while head:
            print(head.val),
            head = head.next

    def deleteDuplicates(self, head):
        # iterate through to find the count of all values:
        #. append values to list
        # create count dict:

        # base case: - return if head if head == None or head.next == None:
        if not head or not head.next:
            return head

        start = head
        R = []
        while start:
            R.append(start.val)
            start = start.next

        # Now create a count array:
        D = {}
        for v in list(set(R)):
            D[v] = R.count(v)


        dummy = ListNode(None)
        dummy.next = head

        head = dummy

        while head.next:
            if D[head.next.val] > 1:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next



S = Solution()
S.printL(head)
print('\n')
x = S.deleteDuplicates(head)
S.printL(x)

