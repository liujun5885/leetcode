// Definition for singly-linked list.

use std::cell::RefCell;

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn build_list_from_vec(val_vec: Vec<i32>) -> Option<Box<ListNode>> {
        if val_vec.is_empty() {
            return None;
        }

        let mut root = Some(Box::new(ListNode { val: val_vec[0], next: None }));
        let mut ptr = &mut root;

        for i in 1..val_vec.len() {
            let node = Some(Box::new(ListNode { val: val_vec[i], next: None }));
            if let Some(n) = ptr {
                n.next = node;
                ptr = &mut n.next;
            }
        }

        return root;
    }
}

struct Solution;

impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let mut buf = vec![1];
        let mut next = head.take();
        let root = RefCell::new(&next);
        head.replace(root.as_ptr().unwrap());

        let mut i = 0;
        let mut j = buf.len() - 1;
        while i < j {
            i += 1;
            j -= 1;
        }
        if i == j {}
    }
}

#[cfg(test)]
mod tests {
    use crate::{Solution, ListNode};

    #[test]
    fn it_works() {
        let val_list = vec![1, 2, 3, 4, 5, 6];
        let mut root = ListNode::build_list_from_vec(val_list);
        Solution::reorder_list(&mut root);
        let expected = vec![1, 6, 2, 5, 3, 4];
        let mut output = vec![];

        while let Some(head) = &root {
            output.push(head.val);
            root = head.next.clone();
        }

        assert_eq!(output, expected);
    }
}