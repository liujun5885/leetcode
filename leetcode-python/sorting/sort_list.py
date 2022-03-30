# https://leetcode-cn.com/problems/sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head
        mid = None
        while end is not None:
            mid = start
            start = start.next
            if end.next is None:
                end = None
            else:
                end = end.next.next
        return mid

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        mid = self.getMiddle(head)
        mid_next = mid.next
        mid.next = None
        upper_sorted_list = self.sortList(head)
        lower_sorted_list = self.sortList(mid_next)

        root = ListNode()
        cur = root

        upper_cur, lower_cur = upper_sorted_list, lower_sorted_list
        while upper_cur is not None and lower_cur is not None:
            if upper_cur.val < lower_cur.val:
                cur.next = upper_cur
                upper_cur = upper_cur.next
            else:
                cur.next = lower_cur
                lower_cur = lower_cur.next
            cur = cur.next

        while upper_cur is not None:
            cur.next = upper_cur
            upper_cur = upper_cur.next
            cur = cur.next

        while lower_cur is not None:
            cur.next = lower_cur
            lower_cur = lower_cur.next
            cur = cur.next
        return root.next
