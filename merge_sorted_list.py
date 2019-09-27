

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
# Super code for converting a list to a linked list:

class LinkedList:
	def __init__(self, first, next=()):
		self.first = first
		self.next = next

def listToLinkedList(lst):
	assert len(lst) > 0
	if len(lst) == 1:
		return LinkedList(lst[0])
	else:
		return LinkedList(lst[0], listToLinkedList(lst[1:]))
        
"""

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

        if l1 != None:
            ans.append(l1)
        if l2 != None:
            ans.append(l2) 

        for L in ans:
            while L.next != None:
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
        

        if first == None:
            return None
        else:
            return first

L = Solution()
x = L.mergeTwoLists(l1, l2)
print(x.val, x.next.val, x.next.next.val)