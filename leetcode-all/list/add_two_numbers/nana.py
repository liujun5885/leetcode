# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
           return l2
        if l2 is None:
           return l1
        flag = 0
        tmp = ListNode(0)
        res = tmp
        while l1 or l2:
            sum = 0
            if l1:
               sum = l1.val
               l1 = l1.next
            if l2:
               sum += l2.val
               l2 = l2.next
            tmp_val = (sum + flag)%10 
            flag = (sum + flag)//10
            res.next = ListNode(tmp_val)
            res = res.next
        if flag:
            res.next = ListNode(flag)
        res = tmp.next
        return res
