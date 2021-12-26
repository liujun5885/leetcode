// https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation/

struct Solution;

impl Solution {
    pub fn max_sum_after_operation(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![vec![0; 2]; n];

        dp[0][0] = nums[0];
        dp[0][1] = nums[0] * nums[0];
        let mut max = std::cmp::max(dp[0][0], dp[0][1]);
        for i in 1..n {
            dp[i][0] = std::cmp::max(dp[i - 1][0] + nums[i], nums[i]);
            dp[i][1] = std::cmp::max(
                std::cmp::max(dp[i - 1][1] + nums[i], dp[i - 1][0] + nums[i] * nums[i]),
                nums[i] * nums[i],
            );
            max = std::cmp::max(std::cmp::max(dp[i][0], dp[i][1]), max);
        }
        println!("{:?}", dp);
        max
    }
}

#[cfg(test)]
mod tests {
    use crate::maximum_subarray_sum_after_one_operation::Solution;
    #[test]
    fn case01() {
        let actual = Solution::max_sum_after_operation(vec![2, -1, -4, -3]);
        let expected = 17;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let actual = Solution::max_sum_after_operation(vec![1, -1, 1, 1, -1, -1, 1]);
        let expected = 4;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let actual = Solution::max_sum_after_operation(vec![-44]);
        let expected = 1936;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let actual = Solution::max_sum_after_operation(vec![
            -4, -49, -12, -75, -48, 46, 72, 10, 51, -51, 26, -74, 70, -1, -25, 29, 27,
        ]);
        let expected = 5757;
        assert_eq!(actual, expected);
    }
}
