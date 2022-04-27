// https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
use std::collections::{HashSet};

struct Solution {}

impl Solution {
    pub fn find_repeat_number(nums: Vec<i32>) -> i32 {
        let mut hs = HashSet::new();

        for i in nums {
            if hs.contains(&i) {
                return i;
            } else {
                hs.insert(i);
            }
        }
        return -1;
    }
}

#[cfg(test)]
mod test {
    use crate::hash_table::shu_zu_zhong_zhong_fu_de_shu_zi_lcof::Solution;

    #[test]
    fn case01() {
        let nums = vec![2, 3, 1, 0, 2, 5, 3];
        let actual = Solution::find_repeat_number(nums);
        let expected = 2;
        assert_eq!(actual, expected);
    }
}