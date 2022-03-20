# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node_list = []
        p = head
        while p != None:
            node = p
            p = p.next
            node.next = None
            node_list.append(node)

        n = len(node_list)
        if n < 2:
            return

        p = head
        p.next = node_list[n - 1]
        p = p.next
        l, r = 1, n - 2
        while l < r:
            p.next = node_list[l]
            p = p.next
            p.next = node_list[r]
            p = p.next
            l += 1
            r -= 1

        if l == r:
            p.next = node_list[l]
