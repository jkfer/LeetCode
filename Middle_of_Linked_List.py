# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        if not head or not head.next:
            return head

        ref = head
        count = 0

        while head:
            head = head.next
            count += 1

        head = ref
        i = 0
        mid = count // 2

        while i < mid:
            head = head.next
            i += 1
        return head
