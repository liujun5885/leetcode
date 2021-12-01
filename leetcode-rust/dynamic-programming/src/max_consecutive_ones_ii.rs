// https://leetcode-cn.com/problems/max-consecutive-ones-ii/
struct Solution;

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut ones = Vec::new();
        let mut tmp = 0;
        let mut has_zero = false;
        for i in nums.iter() {
            if *i == 1 {
                tmp += 1;
            } else {
                ones.push(tmp);
                tmp = 0;
                has_zero = true;
            }
        }
        if nums[nums.len() - 1] != 0 {
            ones.push(tmp);
        }
        let mut max = ones[0];
        for i in 1..ones.len() {
            max = std::cmp::max(max, ones[i] + ones[i - 1]);
        }
        if has_zero {
            max + 1
        } else {
            max
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::max_consecutive_ones_ii::Solution;
    #[test]
    fn case01() {
        let actual = Solution::find_max_consecutive_ones(vec![1, 0, 1, 1, 0]);
        let expected = 4;
        assert_eq!(actual, expected);
    }
}
