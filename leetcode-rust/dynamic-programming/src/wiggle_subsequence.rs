// https://leetcode-cn.com/problems/wiggle-subsequence/

struct Solution;

impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![vec![0; 2]; n];
        if n <= 1 {
            return n as i32;
        }

        for i in 1..n {
            if nums[i] - nums[i - 1] > 0 {
                dp[i][0] = std::cmp::max(dp[i - 1][1] + 1, dp[i - 1][0]);
                dp[i][1] = dp[i - 1][1];
            } else if nums[i] - nums[i - 1] < 0 {
                dp[i][1] = std::cmp::max(dp[i - 1][0] + 1, dp[i - 1][1]);
                dp[i][0] = dp[i - 1][0];
            } else {
                dp[i][1] = dp[i - 1][1];
                dp[i][0] = dp[i - 1][0];
            }
        }
        std::cmp::max(dp[n - 1][0], dp[n - 1][1]) + 1
    }
}

#[cfg(test)]
mod tests {
    use crate::wiggle_subsequence::Solution;

    #[test]
    fn case01() {
        let actual = Solution::wiggle_max_length(vec![1, 7, 4, 9, 2, 5]);
        let expected = 6;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let actual = Solution::wiggle_max_length(vec![1, 17, 5, 10, 13, 15, 10, 5, 16, 8]);
        let expected = 7;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let actual = Solution::wiggle_max_length(vec![1, 2, 3, 4, 5, 6, 7, 8, 9]);
        let expected = 2;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let actual = Solution::wiggle_max_length(vec![0, 0]);
        let expected = 1;
        assert_eq!(actual, expected);
    }
}
