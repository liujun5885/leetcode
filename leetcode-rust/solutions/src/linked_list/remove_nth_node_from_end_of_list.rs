use crate::utils::list_node::ListNode;

struct Solution;

impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut cur = head;
        let mut reversed: Option<Box<ListNode>> = None;
        while let Some(mut node) = cur {
            cur = node.next;
            node.next = reversed;
            reversed = Some(node);
        }

        cur = Some(Box::new(ListNode {
            val: 0,
            next: reversed,
        }));
        reversed = None;
        let mut i = 0;
        while let Some(mut node) = cur {
            if i == n - 1 {
                node.next = node.next.unwrap().next;
            }
            cur = node.next;
            node.next = reversed;
            if i > 0 {
                reversed = Some(node);
            } else {
                reversed = None;
            }
            i += 1;
        }
        return reversed;
    }
}

#[cfg(test)]
mod test {
    use crate::linked_list::remove_nth_node_from_end_of_list::Solution;
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let head = vec![1, 2, 3, 4, 5];
        let n = 2;
        let actual = Solution::remove_nth_from_end(ListNode::from_vec(&head), n);
        let expected = vec![1, 2, 3, 5];
        assert_eq!(actual.unwrap().convert_to_vec(), expected)
    }

    #[test]
    fn case02() {
        let head = vec![1];
        let n = 1;
        let actual = Solution::remove_nth_from_end(ListNode::from_vec(&head), n);
        assert_eq!(actual, None)
    }
}
