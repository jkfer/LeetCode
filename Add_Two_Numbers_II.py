# https://leetcode.com/problems/add-two-numbers-ii/
# 445
# Medium


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Lstack(self, L):
        s = []
        while L:
            s.append(L.val)
            L = L.next
        return s

    def addTwoNumbers(self, l1, l2):
        S1 = self.Lstack(l1)
        S2 = self.Lstack(l2)
        carry = 0
        ref = head
        head = None

        ref = ListNode()

        while S1 and S2:
            V = S1.pop() + S2.pop() + carry
            carry = V / 10
            r = V % 10
            L = ListNode(r)
            L.next = head
            head = L

        while S1 or S2:
            V = (S1.pop() if S1 else S2.pop()) + carry
            carry = V / 10
            r = V % 10
            L = ListNode(r)
            L.next = head
            head = L

        if carry:
            L = ListNode(carry)
            L.next = head
            head = L

        return head
