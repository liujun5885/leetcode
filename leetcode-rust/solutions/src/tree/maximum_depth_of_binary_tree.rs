// https://leetcode.cn/problems/maximum-depth-of-binary-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(root) => {
                let root = root.borrow();
                1 + std::cmp::max(
                    Solution::max_depth(root.left.clone()),
                    Solution::max_depth(root.right.clone()),
                )
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
            Some(3),
            Some(9),
            Some(20),
            None,
            None,
            Some(15),
            Some(7),
        ]);
        assert_eq!(3, Solution::max_depth(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![Some(1), Some(2)]);
        assert_eq!(2, Solution::max_depth(root));
    }

    #[test]
    fn case03() {
        let root = TreeNode::from_vec(&vec![Some(1), Some(2), Some(1)]);
        assert_eq!(2, Solution::max_depth(root));
    }
}
