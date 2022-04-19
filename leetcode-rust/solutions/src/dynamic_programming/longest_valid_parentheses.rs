// https://leetcode-cn.com/problems/longest-valid-parentheses/

use std::cmp;

struct Solution;
impl Solution {
    pub fn longest_valid_parentheses(s: String) -> i32 {
        let mut dp = vec![0; s.len()];
        let mut result = 0;
        let char_vector: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if char_vector[i] != ')' || i < 1 {
                continue;
            }
            if char_vector[i - 1] == '(' {
                let mut max_length = 0;
                if i >= 2 {
                    max_length = dp[i - 2]
                }
                dp[i] = max_length + 2;
            }
            if char_vector[i - 1] == ')'
                && i - dp[i - 1] >= 1
                && char_vector[i - dp[i - 1] - 1] == '('
            {
                let mut max_length = 0;
                if i - dp[i - 1] > 1 {
                    max_length = dp[i - dp[i - 1] - 2];
                }
                dp[i] = max_length + 2 + dp[i - 1]
            }
            result = cmp::max(result, dp[i])
        }
        println!("{:?}", dp);
        result as i32
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::longest_valid_parentheses::Solution;
    #[test]
    fn case01() {
        let actual = Solution::longest_valid_parentheses(String::from("()(())"));
        let expected = 6;
        assert_eq!(actual, expected);
    }
}
