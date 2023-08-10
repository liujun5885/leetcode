// https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

use crate::utils::list_node::ListNode;

struct Solution;

impl Solution {
    pub fn delete_duplicates(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return head;
        }
        let mut head = head;
        let mut cur = head.as_mut().unwrap();
        let mut prev_val = cur.val;

        while let Some(node) = cur.next.take() {
            if prev_val == node.val {
                cur.next = node.next;
            } else {
                prev_val = node.val;
                cur.next = Some(node);
                cur = cur.next.as_mut().unwrap();
            }
        }
        return head;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let vec = vec![1, 1, 2];
        let actual = Solution::delete_duplicates(ListNode::from_vec(&vec)).unwrap();
        assert_eq!(vec![1, 2], actual.convert_to_vec());
    }
    #[test]
    fn case02() {
        let actual = Solution::delete_duplicates(None);
        assert_eq!(None, actual);
    }
}
