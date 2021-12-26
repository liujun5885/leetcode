// https://leetcode-cn.com/problems/maximum-subarray/

struct Solution;
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max = i32::MIN;
        let mut dp = vec![0; nums.len() + 1];
        for i in 1..nums.len() + 1 {
            if nums[i - 1] > dp[i - 1] + nums[i - 1] {
                dp[i] = nums[i - 1];
            } else {
                dp[i] = dp[i - 1] + nums[i - 1];
            }
            max = std::cmp::max(max, dp[i]);
        }
        return max;
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::maximum_subarray::Solution;
    #[test]
    fn case01() {
        let nums = vec![-2, 1, -3, 4, -1, 2, 1, -5, 4];
        let actual = Solution::max_sub_array(nums);
        let expected = 6;
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_02() {
        let nums = vec![0];
        let actual = Solution::max_sub_array(nums);
        let expected = 0;
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_03() {
        let nums = vec![-2, 1];
        let actual = Solution::max_sub_array(nums);
        let expected = 1;
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_04() {
        let nums = vec![8, -19, 5, -4, 20];
        let actual = Solution::max_sub_array(nums);
        let expected = 21;
        assert_eq!(expected, actual);
    }
}
