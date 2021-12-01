# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def __init__(self):
        self.carry = 0
        self.new_node = ListNode()
        self.new_node_next = self.new_node

    def calculate_val_and_carry(self, num: int) -> (int, int):
        if num >= 10:
            carry = 1
            val = num - 10
        else:
            carry = 0
            val = num
        return val, carry

    def addition_with_carry(self, val1, val2, carry):
        if carry:
            val = val1 + val2 + carry
        else:
            val = val1 + val2
        return self.calculate_val_and_carry(val)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        if not node1 and not node2:
            self.new_node_next.next = ListNode(val=self.carry) if self.carry > 0 else None
            return self.new_node.next

        elif node1 and not node2:
            val, self.carry = self.addition_with_carry(node1.val, 0, self.carry)
            self.new_node_next.next = ListNode(val=val)
            self.new_node_next = self.new_node_next.next
            return self.addTwoNumbers(node1.next, None)

        elif node2 and not node1:
            return self.addTwoNumbers(node2, None)

        val, self.carry = self.addition_with_carry(node1.val, node2.val, self.carry)
        self.new_node_next.next = ListNode(val=val)
        self.new_node_next = self.new_node_next.next

        return self.addTwoNumbers(node1.next, node2.next)