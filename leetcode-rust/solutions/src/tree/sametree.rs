// https://leetcode.cn/problems/same-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;
struct Solution;
impl Solution {
    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(p), Some(q)) => {
                let p = p.borrow();
                let q = q.borrow();
                p.val == q.val
                    && Solution::is_same_tree(p.left.clone(), q.left.clone())
                    && Solution::is_same_tree(p.right.clone(), q.right.clone())
            }
            _ => false,
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let p = TreeNode::from_vec(&vec![Some(1), Some(2), Some(3)]);
        let q = TreeNode::from_vec(&vec![Some(1), Some(2), Some(3)]);
        assert_eq!(true, Solution::is_same_tree(p, q));
    }

    #[test]
    fn case02() {
        let p = TreeNode::from_vec(&vec![Some(1), Some(2)]);
        let q = TreeNode::from_vec(&vec![Some(1), None, Some(2)]);
        assert_eq!(false, Solution::is_same_tree(p, q));
    }

    #[test]
    fn case03() {
        let p = TreeNode::from_vec(&vec![Some(1), Some(2), Some(1)]);
        let q = TreeNode::from_vec(&vec![Some(1), Some(1), Some(2)]);
        assert_eq!(false, Solution::is_same_tree(p, q));
    }
}
