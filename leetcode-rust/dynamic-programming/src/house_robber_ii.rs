struct Solution;

impl Solution {
    pub fn rob_1(nums: &Vec<i32>, start: usize, end: usize) -> i32 {
        let length = end - start;

        let mut dp = vec![0; length + 1];
        dp[1] = nums[start];

        for i in 2..length + 1 {
            dp[i] = std::cmp::max(dp[i - 1], dp[i - 2] + nums[start + i - 1]);
        }

        dp[length]
    }

    pub fn rob(nums: Vec<i32>) -> i32 {
        match nums.len() {
            2 => return std::cmp::max(nums[0], nums[1]),
            1 => return nums[0],
            0 => return 0,
            _ => {}
        }
        std::cmp::max(
            Solution::rob_1(&nums, 0, nums.len() - 1),
            Solution::rob_1(&nums, 1, nums.len()),
        )
    }
}

#[cfg(test)]
mod tests {
    use crate::house_robber_ii::Solution;
    #[test]
    fn case01() {
        let actual = Solution::rob(vec![2, 3, 2]);
        let expected = 3;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case02() {
        let actual = Solution::rob(vec![1, 2, 3, 1]);
        let expected = 4;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case03() {
        let actual = Solution::rob(vec![1]);
        let expected = 1;
        assert_eq!(actual, expected);
    }
}
