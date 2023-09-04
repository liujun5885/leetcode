// https://leetcode.cn/problems/balanced-binary-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn helper(root: Option<Rc<RefCell<TreeNode>>>) -> (bool, i32) {
            match root {
                None => (true, 0),
                Some(root) => {
                    let root = root.borrow();
                    let (left_balanced, left_depth) = helper(root.left.clone());
                    let (right_balanced, right_depth) = helper(root.right.clone());
                    (
                        left_balanced && right_balanced && (left_depth - right_depth).abs() <= 1,
                        std::cmp::max(left_depth, right_depth) + 1,
                    )
                }
            }
        }
        helper(root).0
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let root = TreeNode::from_vec(&vec![
            Some(3),
            Some(9),
            Some(20),
            None,
            None,
            Some(15),
            Some(7),
        ]);
        assert_eq!(true, Solution::is_balanced(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![
            Some(1),
            Some(2),
            Some(2),
            Some(3),
            Some(3),
            None,
            None,
            Some(4),
            Some(4),
        ]);
        assert_eq!(false, Solution::is_balanced(root));
    }

    #[test]
    fn case03() {
        let root = TreeNode::from_vec(&vec![Some(1), Some(2), Some(1)]);
        assert_eq!(true, Solution::is_balanced(root));
    }
}
