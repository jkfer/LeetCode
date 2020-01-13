# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# 1290


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head):
        # get number:
        N = []
        while head:
            N.append(head.val)
            head = head.next

        p = 0
        ans = 0
        for i in N[::-1]:
            ans += i * (2 ** p)
            p += 1

        return ans
