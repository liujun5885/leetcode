// https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

use crate::utils::tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution;
impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn helper(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if nums.is_empty() {
                return None;
            }

            let mid = nums.len() / 2;
            let mut root = TreeNode::new(nums[mid]);
            root.left = helper(&nums[..mid]);
            root.right = helper(&nums[mid + 1..]);
            Some(Rc::new(RefCell::new(root)))
        }

        helper(&nums)
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::utils::tree_node::TreeNode;

    #[test]
    fn case01() {
        let nums = vec![-10, -3, 0, 5, 9];
        let root = TreeNode::from_vec(&vec![Some(0), Some(-3), Some(9), Some(-10), None, Some(5)]);
        assert_eq!(root, Solution::sorted_array_to_bst(nums));
    }

    #[test]
    fn test02() {
        let nums = vec![1, 3];
        let root = TreeNode::from_vec(&vec![Some(3), Some(1)]);
        assert_eq!(root, Solution::sorted_array_to_bst(nums));
    }
}
