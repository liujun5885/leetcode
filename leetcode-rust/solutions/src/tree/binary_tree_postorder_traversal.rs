// https://leetcode.cn/problems/binary-tree-postorder-traversal/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        fn helper(root: Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
            match root {
                Some(root) => {
                    let root = root.borrow();
                    helper(root.left.clone(), result);
                    helper(root.right.clone(), result);
                    result.push(root.val);
                }
                None => {}
            }
        }
        let mut result = vec![];
        helper(root, &mut result);
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let root = TreeNode::from_vec(&vec![Some(1), None, Some(2), Some(3)]);
        let expected = vec![3, 2, 1];
        assert_eq!(expected, Solution::postorder_traversal(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![
            Some(1),
            Some(2),
            Some(3),
            Some(4),
            Some(5),
            Some(6),
            Some(7),
        ]);
        let expected = vec![4, 5, 2, 6, 7, 3, 1];
        assert_eq!(expected, Solution::postorder_traversal(root));
    }
}
