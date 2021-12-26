// https://leetcode-cn.com/problems/toss-strange-coins/

struct Solution;

impl Solution {
    pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
        let n = prob.len();
        let mut dp = vec![vec![0.0; target as usize + 1]; n];

        dp[0][0] = 1.0 - prob[0];
        if target > 0 {
            dp[0][1] = prob[0];
        }

        for i in 1..n {
            dp[i][0] = dp[i - 1][0] * (1.0 - prob[i]);
            for j in 1..target as usize + 1 {
                if prob[i] > 0.0 {
                    dp[i][j] = dp[i - 1][j - 1] * prob[i] + dp[i - 1][j] * (1.0 - prob[i]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        println!("{:?}", dp);
        dp[n - 1][target as usize]
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::toss_strange_coins::Solution;
    use float_cmp::approx_eq;
    #[test]
    fn case01() {
        let prob = vec![0.4];
        let target = 1;
        let actual = Solution::probability_of_heads(prob, target);
        let expected = 0.4;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let prob = vec![0.5, 0.5, 0.5, 0.5, 0.5];
        let target = 0;
        let actual = Solution::probability_of_heads(prob, target);
        let expected = 0.03125;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let prob = vec![0.2, 0.8, 0.0, 0.3, 0.5];
        let target = 3;
        let actual = Solution::probability_of_heads(prob, target);
        let expected = 0.182;
        assert!(approx_eq!(f64, actual, expected));
    }
}
