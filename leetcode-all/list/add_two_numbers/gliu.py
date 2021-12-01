

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        header1 = ListNode(next = l1)
        header2 = ListNode(next = l2)
        result_header = header1
        while header1.next is not None and header2.next is not None:
            header1.next.val += header2.next.val + (1 if carry else 0)
            carry = header1.next.val > 9
            if carry:
                header1.next.val -= 10
            header1 = header1.next
            header2 = header2.next
        if header1.next is None:
            header1.next = header2.next
        while carry and header1.next is not None and header1.next.val == 9:
            header1.next.val = 0
            header1 = header1.next
        if carry:
            if header1.next is None:
                header1.next = ListNode(val=1)
            else:
                header1.next.val += 1
        return result_header.next


