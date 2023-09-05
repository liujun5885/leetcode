// https://leetcode.cn/problems/remove-linked-list-elements/

use crate::utils::list_node::ListNode;

struct Solution;
impl Solution {
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut head = ListNode { val: 0, next: head };
        let mut cur = &mut head;
        while let Some(ref mut node) = cur.next {
            if node.val == val {
                cur.next = node.next.take();
            } else {
                cur = cur.next.as_mut()?;
            }
        }
        head.next
    }
}

#[cfg(test)]
mod test {
    use crate::linked_list::remove_linked_list_elements::Solution;
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let head = ListNode::from_vec(&vec![1, 2, 6, 3, 4, 5, 6]);
        let val = 6;
        let expected = ListNode::from_vec(&vec![1, 2, 3, 4, 5]);
        assert_eq!(expected, Solution::remove_elements(head, val));
    }

    #[test]
    fn case02() {
        let head = ListNode::from_vec(&vec![]);
        let val = 1;
        let expected = ListNode::from_vec(&vec![]);
        assert_eq!(expected, Solution::remove_elements(head, val));
    }

    #[test]
    fn case03() {
        let head = ListNode::from_vec(&vec![7, 7, 7, 7]);
        let val = 7;
        let expected = ListNode::from_vec(&vec![]);
        assert_eq!(expected, Solution::remove_elements(head, val));
    }

    #[test]
    fn case04() {
        let head = ListNode::from_vec(&vec![7, 7, 7, 7, 1]);
        let val = 7;
        let expected = ListNode::from_vec(&vec![1]);
        assert_eq!(expected, Solution::remove_elements(head, val));
    }
}
