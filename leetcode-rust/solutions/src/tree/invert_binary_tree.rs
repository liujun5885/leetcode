// https://leetcode.cn/problems/invert-binary-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root {
            let left = node.borrow().left.clone();
            let right = node.borrow().right.clone();
            node.borrow_mut().left = Self::invert_tree(right);
            node.borrow_mut().right = Self::invert_tree(left);
            Some(node)
        } else {
            None
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
            Some(4),
            Some(2),
            Some(7),
            Some(1),
            Some(3),
            Some(6),
            Some(9),
        ]);
        let expected = TreeNode::from_vec(&vec![
            Some(4),
            Some(7),
            Some(2),
            Some(9),
            Some(6),
            Some(3),
            Some(1),
        ]);
        assert_eq!(expected, Solution::invert_tree(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![Some(2), Some(1), Some(3)]);
        let expected = TreeNode::from_vec(&vec![Some(2), Some(3), Some(1)]);
        assert_eq!(expected, Solution::invert_tree(root));
    }

    #[test]
    fn test03() {
        let root = TreeNode::from_vec(&vec![]);
        let expected = TreeNode::from_vec(&vec![]);
        assert_eq!(expected, Solution::invert_tree(root));
    }
}
