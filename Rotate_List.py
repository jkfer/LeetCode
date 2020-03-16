# https://leetcode.com/problems/rotate-list/
# 61
# medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def Lprint(self, head):
        while head:
            print(head.val),
            head = head.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # get length of the linked list:
        orig_head = head

        # Get the length of the list node
        ll = 0
        while head:
            head = head.next
            ll += 1

        # if k > ll, we only have to rotate
        if k % ll == 0:
            return orig_head

        # Interception point - should be ll - k
        k = ll - (k % ll)

        ref = orig_head

        # get to intercepting point
        count = 1
        while count < k:
            orig_head = orig_head.next
            count += 1

        fir = orig_head.next
        orig_head.next = None

        ans = fir

        while fir.next:
            fir = fir.next

        fir.next = ref

        return ans
