// Definition for a binary tree node.
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> TreeNode {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }

    pub fn from_vec(vec: &Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        if vec.is_empty() {
            return None;
        }
        let head = Rc::new(RefCell::new(TreeNode::new(vec[0].unwrap())));

        let mut queue = std::collections::VecDeque::new();
        queue.push_back(head.clone());
        let mut i = 1;
        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            if i < vec.len() && vec[i].is_some() {
                let left = Rc::new(RefCell::new(TreeNode::new(vec[i].unwrap())));
                node.borrow_mut().left = Some(left.clone());
                queue.push_back(left);
            }
            i += 1;
            if i < vec.len() && vec[i].is_some() {
                let right = Rc::new(RefCell::new(TreeNode::new(vec[i].unwrap())));
                node.borrow_mut().right = Some(right.clone());
                queue.push_back(right);
            }
            i += 1;
        }

        Some(head)
    }

    pub fn to_vec(&self) -> Vec<Option<i32>> {
        let mut result = Vec::new();

        let mut queue = std::collections::VecDeque::new();
        queue.push_back(Some(Rc::new(RefCell::new(self.clone()))));

        while let Some(option_node) = queue.pop_front() {
            if let Some(node) = option_node {
                result.push(Some(node.clone().borrow().val));

                if let Some(left) = node.borrow().left.clone() {
                    queue.push_back(Some(left));
                } else {
                    queue.push_back(None)
                }

                if let Some(right) = node.borrow().right.clone() {
                    queue.push_back(Some(right));
                } else {
                    queue.push_back(None)
                }
            } else {
                result.push(None);
            }
        }

        while result.last() == Some(&None) {
            result.pop();
        }

        result
    }
}

#[cfg(test)]
mod test {
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let vec = vec![Some(1), Some(2), None, Some(3), None, Some(4), None, Some(5)];
        let head = TreeNode::from_vec(&vec).unwrap();
        assert_eq!(vec, head.borrow().to_vec());
    }

    #[test]
    fn case02() {
        let vec = vec![Some(1), Some(2), Some(3), Some(4), Some(5)];
        let head = TreeNode::from_vec(&vec).unwrap();
        assert_eq!(vec, head.borrow().to_vec());
    }
}
