// https://leetcode.cn/problems/symmetric-tree/

struct Solution;
use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn is_mirror(
        left: Option<Rc<RefCell<TreeNode>>>,
        right: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (left, right) {
            (None, None) => true,
            (Some(left), Some(right)) => {
                let left = left.borrow();
                let right = right.borrow();

                left.val == right.val
                    && Solution::is_mirror(left.left.clone(), right.right.clone())
                    && Solution::is_mirror(left.right.clone(), right.left.clone())
            }
            _ => false,
        }
    }

    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match root {
            None => true,
            Some(root) => {
                let root = root.borrow();
                Solution::is_mirror(root.left.clone(), root.right.clone())
            }
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let root = TreeNode::from_vec(&vec![
            Some(1),
            Some(2),
            Some(2),
            Some(3),
            Some(4),
            Some(4),
            Some(3),
        ]);
        assert_eq!(true, Solution::is_symmetric(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![
            Some(1),
            Some(2),
            Some(2),
            None,
            Some(3),
            None,
            Some(3),
        ]);
        assert_eq!(false, Solution::is_symmetric(root));
    }
}
