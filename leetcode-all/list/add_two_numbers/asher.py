class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        p = result
        while l1 is not None or l2 is not None:
            middle = (l1.val if l1 else 0) + (l2.val if l2 else 0) + p.val
            p.val = middle % 10
            if (l1 and l1.next) or (l2 and l2.next) or middle // 10 > 0:
                p.next = ListNode(middle // 10)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result


def list_to_chain(l):
    start = ListNode(l[0])
    p = start
    for i in l[1:]:
        node = ListNode(i)
        p.next = node
        p = node
    return start


def print_chain(chain):
    start = chain
    while start != None:
        print(start.val)
        start = start.next


if __name__ == '__main__':
    l1 = list_to_chain([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_chain([9, 9, 9, 9])
    print_chain(Solution().addTwoNumbers(l1, l2))
