# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Medium
# 82


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(5)


class Solution:
    def Lprint(self, head):
        while head:
            print(head.val, end=",")
            head = head.next

    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        mem = []

        # address the first two nodes to not be the same
        while head.val == head.next.val:
            x = head.val
            mem.append(x)
            while head and head.val == x:
                head = head.next

            if not head:
                return None
            elif not head.next:
                if head.val in mem:
                    return None
                else:
                    return head

        ref = head

        prev = ref
        nex = head.next

        while nex:
            matched = False

            if nex.next and nex.val == nex.next.val:
                matched = True
                N = nex.val
                while nex and nex.val == N:
                    nex = nex.next

            if matched:
                prev.next = nex
            else:
                prev = nex
                nex = prev.next

        return ref


S = Solution()
# S.Lprint(head)

X = S.deleteDuplicates(head)
S.Lprint(X)
