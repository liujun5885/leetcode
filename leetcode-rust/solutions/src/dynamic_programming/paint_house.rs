// https://leetcode-cn.com/problems/paint-house/

struct Solution;

impl Solution {
    pub fn min_cost(costs: Vec<Vec<i32>>) -> i32 {
        let mut min = i32::MAX;
        let mut dp = vec![vec![0; 3]; costs.len() + 1];

        dp[1][0] = costs[0][0];
        dp[1][1] = costs[0][1];
        dp[1][2] = costs[0][2];

        for i in 1..costs.len() + 1 {
            dp[i][0] = std::cmp::min(dp[i - 1][1], dp[i - 1][2]) + costs[i - 1][0];
            dp[i][1] = std::cmp::min(dp[i - 1][0], dp[i - 1][2]) + costs[i - 1][1];
            dp[i][2] = std::cmp::min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1][2];
            min = dp[i][0].min(dp[i][1]).min(dp[i][2])
        }

        min
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::paint_house::Solution;
    #[test]
    fn case01() {
        let costs = vec![vec![17, 2, 17], vec![16, 16, 5], vec![14, 3, 19]];
        let actual = Solution::min_cost(costs);
        let expected = 10;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case02() {
        let costs = vec![vec![7, 6, 2]];
        let actual = Solution::min_cost(costs);
        let expected = 2;
        assert_eq!(actual, expected);
    }
}
