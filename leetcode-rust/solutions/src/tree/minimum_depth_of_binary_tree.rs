// https://leetcode.cn/problems/minimum-depth-of-binary-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn min_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            None => 0,
            Some(root) => {
                let root = root.borrow();
                match (root.left.clone(), root.right.clone()) {
                    (None, None) => 1,
                    (None, Some(right)) => 1 + Solution::min_depth(Some(right)),
                    (Some(left), None) => 1 + Solution::min_depth(Some(left)),
                    (Some(left), Some(right)) => {
                        1 + std::cmp::min(
                            Solution::min_depth(Some(left)),
                            Solution::min_depth(Some(right)),
                        )
                    }
                }
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
        assert_eq!(2, Solution::min_depth(root));
    }

    #[test]
    fn case02() {
        let root = TreeNode::from_vec(&vec![
            Some(2),
            None,
            Some(3),
            None,
            Some(4),
            None,
            Some(5),
            None,
            Some(6),
        ]);
        assert_eq!(5, Solution::min_depth(root));
    }
}
