# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        pA = headA
        pB = headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next
        if lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next
        else:
            for _ in range(lenA - lenB):
                headA = headA.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA