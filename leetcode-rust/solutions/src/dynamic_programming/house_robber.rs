// https://leetcode-cn.com/problems/house-robber/

struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut dp = vec![0; nums.len() + 1];
        dp[1] = nums[0];

        for i in 2..nums.len() + 1 {
            dp[i] = std::cmp::max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }

        dp[nums.len()]
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::house_robber::Solution;
    #[test]
    fn case01() {
        let actual = Solution::rob(vec![1, 2, 3, 1]);
        let expected = 4;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case_02() {
        let actual = Solution::rob(vec![2, 7, 9, 3, 1]);
        let expected = 12;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case_03() {
        let actual = Solution::rob(vec![2, 1, 1, 2]);
        let expected = 4;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case_04() {
        let actual = Solution::rob(vec![1, 3, 1]);
        let expected = 3;
        assert_eq!(actual, expected);
    }
}
