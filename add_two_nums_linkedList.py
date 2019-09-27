from math import pow

#Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Input:
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(l2.val)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        res = 0
        for L in l1, l2:
            count = 0
            while L.next != None:
                res += int(L.val * pow(10, count))
                L = L.next
                count +=1
            res += int(L.val * pow(10, count))
        
        # print(res)
        
        l3 = ListNode(int(list(str(res))[0]))

        for i in list(str(res))[1:]:
            l3.next = ListNode(int(i))
            l3 = l3.next
        
        return l3

Solution().addTwoNumbers(l1, l2)

