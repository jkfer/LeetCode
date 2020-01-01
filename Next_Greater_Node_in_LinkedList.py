# https://leetcode.com/problems/next-greater-node-in-linked-list/
# 1019


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


root = ListNode(10)
root.next = ListNode(4)
root.next.next = ListNode(6)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(10)
# root.next.next.next.next.next = ListNode(2)
# root.next.next.next.next.next.next = ListNode(5)
# root.next.next.next.next.next.next.next = ListNode(1)
# Input: [10,4,6,4,10]
# Output: [0,6,10,10,0]


class Solution:
    def Lprint(self, head):
        while head:
            print(head.val, end=", ")
            head = head.next

    # working solution but times out
    # long and complex
    def nextLargerNodes(self, head):
        mem = []
        ANS = []
        count = 0
        save_node = None
        end = False

        while head:
            ref = head
            v = head.val
            found = False

            if not head.next:
                ANS.append(0)
                found = True

            if len(mem) > count+1 and not found:
                for n in mem[count+1:]:
                    if n > v:
                        ANS.append(n)
                        found = True
                        break

            if not save_node:
                c_node = head
            else:
                c_node = save_node

            while c_node and not found and not end:
                c = c_node.val

                if c > v:
                    ANS.append(c)
                    found = True
                    save_node = c_node.next
                    # count += 1

                mem.append(c)
                c_node = c_node.next
                if not c_node:
                    end = True
                    save_node = None

            if not found:
                ANS.append(0)

            head = ref.next
            count += 1
            # print(mem, ANS)
        return ANS

    # referred solution:
    """
    Idea: As you traverse the linked list - add it to a stack with position.
    When you find a value greater than the last value in stack
    append that value with relevant position to answer
    """
    def nextLargerNodes2(self, head):
        pos = -1
        stack = []
        ans = []

        while head:
            pos += 1
            ans.append(0)

            while stack and stack[-1][1] < head.val:
                p, val = stack.pop()
                ans[p] = head.val

            stack.append([pos, head.val])
            head = head.next
        return ans


S = Solution()
# S.Lprint(root)
H = S.nextLargerNodes2(root)
print(H)
