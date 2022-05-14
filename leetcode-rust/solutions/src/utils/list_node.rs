#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }

    pub fn from_vec(vec: &Vec<i32>) -> Option<Box<ListNode>> {
        if vec.is_empty() {
            return None;
        }

        let mut head: Option<Box<ListNode>> = None;
        let mut cur = &mut head;
        for v in vec.iter() {
            let item = Box::new(ListNode::new(*v));
            cur.replace(item);
            if let Some(node) = cur {
                cur = &mut node.next;
            }
        }
        return head;
    }

    pub fn convert_to_vec(self) -> Vec<i32> {
        let mut vec = Vec::new();

        let mut head = Some(Box::new(self));
        while let Some(p) = head {
            vec.push(p.val);
            head = p.next;
        }

        return vec;
    }
}

#[cfg(test)]
mod test {
    use crate::utils::list_node::ListNode;

    #[test]
    fn case01() {
        let vec = vec![1, 2, 3, 4, 5];
        let head = ListNode::from_vec(&vec).unwrap();
        assert_eq!(vec, head.convert_to_vec());
    }
}

