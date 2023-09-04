// https://leetcode.cn/problems/path-sum/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool {
        match root {
            None => false,
            Some(root) => {
                let root = root.borrow();
                if root.left.is_none() && root.right.is_none() {
                    target_sum == root.val
                } else {
                    Solution::has_path_sum(root.left.clone(), target_sum - root.val)
                        || Solution::has_path_sum(root.right.clone(), target_sum - root.val)
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
            Some(5),
            Some(4),
            Some(8),
            Some(11),
            None,
            Some(13),
            Some(4),
            Some(7),
            Some(2),
            None,
            None,
            None,
            Some(1),
        ]);
        assert_eq!(true, Solution::has_path_sum(root, 22));
    }

    #[test]
    fn test02() {
        let root = TreeNode::from_vec(&vec![Some(1), Some(2), Some(3)]);
        assert_eq!(false, Solution::has_path_sum(root, 5));
    }
}
