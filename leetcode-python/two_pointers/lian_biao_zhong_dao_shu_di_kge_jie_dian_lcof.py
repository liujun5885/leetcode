# https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # fast = slow
        fast, slow = head, head
        # fast is k faster than slow
        while fast and k > 0:
            fast = fast.next
            k -= 1
        # if fast go to then end, the slow is k slower than faster
        while fast:
            slow = slow.next
            fast = fast.next

        # return slow
        return slow
