// https://leetcode.cn/problems/swap-nodes-in-pairs/

use crate::utils::list_node::ListNode;

struct Solution;

impl Solution {
    pub fn swap_pairs_v2(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        head.and_then(|mut n| {
            match n.next {
                Some(mut m) => {
                    n.next = Self::swap_pairs_v2(m.next);
                    m.next = Some(n);
                    Some(m)
                }
                None => Some(n)
            }
        })
    }

    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut remain = head;
        let mut result = ListNode::new(0);
        let mut tail = &mut result;
        while let Some(mut n1) = remain {
            remain = n1.next.take(); // take()将n1打断，这样n1只有一个值，返回值是除n1节点外的剩余节点
            if let Some(mut n2) = remain {
                remain = n2.next.take(); // take()将n2打断，n2只有一个值，返回值是除n2节点外的剩余节点
                n2.next = Some(n1);
                tail.next = Some(n2);
                tail = tail.next.as_mut().unwrap().next.as_mut().unwrap();
            } else {
                tail.next = Some(n1);
                tail = tail.next.as_mut().unwrap();
            }
        }
        result.next
    }
}

#[cfg(test)]
mod test {
    use crate::linked_list::swap_nodes_in_pairs::Solution;
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let head = vec![1, 2, 3, 4];
        let actual = Solution::swap_pairs(ListNode::from_vec(&head));
        let expected = vec![2, 1, 4, 3];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case02() {
        let head = vec![1];
        let actual = Solution::swap_pairs(ListNode::from_vec(&head));
        let expected = vec![1];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case03() {
        let head = vec![1, 2, 3, 4, 5];
        let actual = Solution::swap_pairs(ListNode::from_vec(&head));
        let expected = vec![2, 1, 4, 3, 5];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case01_v2() {
        let head = vec![1, 2, 3, 4];
        let actual = Solution::swap_pairs_v2(ListNode::from_vec(&head));
        let expected = vec![2, 1, 4, 3];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case02_v2() {
        let head = vec![1];
        let actual = Solution::swap_pairs_v2(ListNode::from_vec(&head));
        let expected = vec![1];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case03_v2() {
        let head = vec![1, 2, 3, 4, 5];
        let actual = Solution::swap_pairs_v2(ListNode::from_vec(&head));
        let expected = vec![2, 1, 4, 3, 5];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }
}
