// https://leetcode.cn/problems/majority-element/

use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut num_vs_count = HashMap::new();
        let mut result = 0;
        let length = nums.len();
        for num in nums {
            let count = num_vs_count.entry(num).or_insert(1);
            *count += 1;
            if *count > length / 2 {
                result = num;
            }
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let nums = vec![3, 2, 3];
        let expected = 3;
        assert_eq!(expected, Solution::majority_element(nums));
    }

    #[test]
    fn case02() {
        let nums = vec![2, 2, 1, 1, 1, 2, 2];
        let expected = 2;
        assert_eq!(expected, Solution::majority_element(nums));
    }
}
