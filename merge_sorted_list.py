

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = []
        ans = []

        if l1:
            ans.append(l1)
        if l2:
            ans.append(l2)

        for L in ans:
            while L.next:
                x = L.val
                res.append(int(x))
                L = L.next
            res.append(L.val)

        res.sort(key=int)
        print(res)

        first = None
        PrevN = None

        for i, val in enumerate(res):
            currN = ListNode(int(val))
            if first is None:
                first = currN
            if PrevN is not None:
                PrevN.next = currN
            PrevN = currN

        if not first:
            return None
        else:
            return first

    def mergeTwoLists2(self, l1, l2):
        ref = ListNode(0)
        dummy = ref
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return ref.next


L = Solution()
x = L.mergeTwoLists2(l1, l2)
print(x.val, x.next.val, x.next.next.val)
