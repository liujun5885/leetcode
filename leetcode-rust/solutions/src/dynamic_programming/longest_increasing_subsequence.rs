// https://leetcode-cn.com/problems/longest-increasing-subsequence/

struct Solution;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![1; nums.len()];
        let mut ans = 1;
        for i in 1..nums.len() {
            for j in 0..i {
                if nums[j] < nums[i] {
                    dp[i] = dp[i].max(dp[j] + 1);
                }
            }
            ans = ans.max(dp[i]);
        }
        ans
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::longest_increasing_subsequence::Solution;

    #[test]
    fn case01() {
        let nums = vec![10, 9, 2, 5, 3, 7, 101, 18];
        let actual = Solution::length_of_lis(nums);
        let expected = 4;
        assert_eq!(actual, expected);
    }
}
