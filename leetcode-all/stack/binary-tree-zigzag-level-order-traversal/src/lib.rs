use std::rc::Rc;
use std::cell::RefCell;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }

    pub fn build_from_list(val_list: Vec<Option<i32>>, i: usize) -> Option<Rc<RefCell<TreeNode>>> {
        if i >= val_list.len() {
            return None;
        }

        if val_list[i].is_none() {
            return None;
        }

        return Some(Rc::new(RefCell::new(TreeNode {
            val: val_list[i].unwrap(),
            left: TreeNode::build_from_list(val_list.clone(), i * 2 + 1),
            right: TreeNode::build_from_list(val_list.clone(), i * 2 + 2),
        })));
    }
}

struct Solution;

impl Solution {
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut stack = vec![root];
        let mut ret = vec![];

        while !stack.is_empty() {
            let mut level = vec![];
            let mut middle = vec![];
            while !stack.is_empty() {
                let node = stack.pop().unwrap();
                if let Some(n) = node {
                    level.push(n.borrow().val);
                    if ret.len() % 2 == 0 {
                        middle.push(n.borrow_mut().left.take());
                        middle.push(n.borrow_mut().right.take());
                    } else {
                        middle.push(n.borrow_mut().right.take());
                        middle.push(n.borrow_mut().left.take());
                    }
                }
            }
            if !level.is_empty() {
                ret.push(level);
            }
            stack = middle;
        }
        return ret;
    }
}

#[cfg(test)]
mod tests {
    use crate::{Solution, TreeNode};

    #[test]
    fn it_works() {
        let val_list: Vec<Option<i32>> = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let root = TreeNode::build_from_list(val_list, 0);
        let output = Solution::zigzag_level_order(Option::from(root.unwrap()));
        let expected = vec![vec![3], vec![20, 9], vec![15, 7]];
        assert_eq!(output, expected);
    }
}
