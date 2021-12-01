# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = res = ListNode(None, None)
        carry = 0
        while l1 and l2:
            cur = l1.val + l2.val + carry
            carry=0
            if cur>9:
                cur-=10
                carry = 1
            res.next = ListNode(cur)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            remain = l1 or l2
            while remain:
                cur = remain.val + carry
                carry=0
                if cur>9:
                    cur-=10
                    carry = 1
                res.next = ListNode(cur)
                res = res.next
                remain = remain.next
        if carry:
            res.next = ListNode(1)
        return start.next