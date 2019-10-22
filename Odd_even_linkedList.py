# 328 - Medium


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def printL(head):
    while head:
        print(head.val, end=" ")
        head = head.next


# Creating a node to test on:
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)


class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = ListNode(None)
        even = ListNode(None)

        count = 1

        odd_ref = odd
        even_ref = even

        while head:
            if count % 2 == 1:
                odd.next = head
                odd = head
            elif count % 2 == 0:
                even.next = head
                even = head

            count += 1
            head = head.next
            odd.next = None
            even.next = None

        ref = odd_ref.next

        while odd_ref.next:
            odd_ref = odd_ref.next

        odd_ref.next = even_ref.next
        return ref


# printL(root)
S = Solution()
x = S.oddEvenList(root)
printL(x)
