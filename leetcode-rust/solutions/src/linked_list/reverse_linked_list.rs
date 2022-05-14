// https://leetcode-cn.com/problems/reverse-linked-list/

use crate::utils::list_node::ListNode;

struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut h: Option<Box<ListNode>> = None;
        let mut cur = &head;
        while let Some(p) = cur {
            let node = Box::new(ListNode { val: p.val, next: h });
            h = Some(node);
            cur = &p.next;
        }
        return h;
    }
}

#[cfg(test)]
mod test {
    use crate::linked_list::reverse_linked_list::Solution;
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let head = vec![1, 2, 3, 4, 5];
        let actual = Solution::reverse_list(
            ListNode::from_vec(&head));
        let expected = vec![5, 4, 3, 2, 1];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }
}
