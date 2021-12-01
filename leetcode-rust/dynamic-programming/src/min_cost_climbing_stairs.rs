use std::cmp;

struct Solution;
impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut new_const = vec![0, 0];
        new_const.extend(cost);
        let mut dp = vec![0; new_const.len()];
        for i in 2..new_const.len() {
            dp[i] = cmp::min(dp[i - 1] + new_const[i], dp[i - 2] + new_const[i - 1]);
        }
        dp[new_const.len() - 1]
    }
}

#[cfg(test)]
mod tests {
    use crate::min_cost_climbing_stairs::Solution;

    #[test]
    fn case01() {
        let cost = vec![1, 100, 1, 1, 1, 100, 1, 1, 100, 1];
        let actual = Solution::min_cost_climbing_stairs(cost);
        let expected = 6;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let cost = vec![10, 15, 20];
        let actual = Solution::min_cost_climbing_stairs(cost);
        let expected = 15;
        assert_eq!(actual, expected);
    }
}
