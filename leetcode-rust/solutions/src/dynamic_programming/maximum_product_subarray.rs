// https://leetcode-cn.com/problems/maximum-product-subarray/

struct Solution;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![vec![0; 2]; n];
        let mut max = nums[0];
        dp[0][0] = nums[0];
        dp[0][1] = nums[0];
        for i in 1..n {
            dp[i][0] = std::cmp::max(
                std::cmp::max(dp[i - 1][1] * nums[i], dp[i - 1][0] * nums[i]),
                nums[i],
            );
            dp[i][1] = std::cmp::min(
                std::cmp::min(dp[i - 1][1] * nums[i], dp[i - 1][0] * nums[i]),
                nums[i],
            );
            max = std::cmp::max(max, dp[i][0]);
        }
        println!("{:?}", dp);
        max
    }
}

#[cfg(test)]
mod tests {
    use crate::maximum_product_subarray::Solution;
    #[test]
    fn case01() {
        let nums = vec![2, 3, -2, 4];
        let actual = Solution::max_product(nums);
        let expected = 6;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case02() {
        let nums = vec![-2, 0, -1];
        let actual = Solution::max_product(nums);
        let expected = 0;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case03() {
        let nums = vec![-2, 3, -4];
        let actual = Solution::max_product(nums);
        let expected = 24;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let nums = vec![0, 2];
        let actual = Solution::max_product(nums);
        let expected = 2;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case05() {
        let nums = vec![2, -5, -2, -4, 3];
        let actual = Solution::max_product(nums);
        let expected = 24;
        assert_eq!(actual, expected);
    }
}
