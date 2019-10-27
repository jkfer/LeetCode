# 234


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        k = []
        while head:
            k.append(head.val)
            head = head.next

        if k == k[::-1]:
            return True
        else:
            return False
