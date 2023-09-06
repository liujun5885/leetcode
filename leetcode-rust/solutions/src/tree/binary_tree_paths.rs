// https://leetcode.cn/problems/binary-tree-paths/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        if root.is_none() {
            return vec![];
        }
        let node = root.unwrap();

        let mut result = vec![];

        let left_result = Self::binary_tree_paths(node.borrow().left.clone());
        let right_result = Self::binary_tree_paths(node.borrow().right.clone());

        if left_result.is_empty() && right_result.is_empty() {
            result.push(node.borrow().val.to_string());
        } else {
            for path in left_result {
                result.push(format!("{}->{}", node.borrow().val, path));
            }
            for path in right_result {
                result.push(format!("{}->{}", node.borrow().val, path));
            }
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let root = TreeNode::from_vec(&vec![Some(1), Some(2), Some(3), None, Some(5)]);
        let expected = vec!["1->2->5".to_string(), "1->3".to_string()];
        assert_eq!(expected, Solution::binary_tree_paths(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![Some(1), None, Some(2), None, None, Some(3)]);
        let expected = vec!["1->2->3".to_string()];
        assert_eq!(expected, Solution::binary_tree_paths(root));
    }

    #[test]
    fn case03() {
        let root = TreeNode::from_vec(&vec![Some(1)]);
        let expected = vec!["1".to_string()];
        assert_eq!(expected, Solution::binary_tree_paths(root));
    }
}
