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

    # Alternate and faster approach
    def oddEvenList2(self, head):
        if not head or not head.next:
            return head

        EVEN_REF = ListNode(None)
        ODD_REF = ListNode(None)
        EVEN = EVEN_REF
        ANS = head

        while head and head.next:
            curr = head
            nex = head.next

            save = nex.next
            nex.next = None

            EVEN_REF.next = nex
            EVEN_REF = EVEN_REF.next

            head.next = save
            head = head.next

        if head:
            head.next = EVEN.next
            return ANS
        else:
            curr.next = EVEN.next
            return ANS


# printL(root)
S = Solution()
x = S.oddEvenList2(root)
printL(x)
