// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

struct Solution;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        // 0 - most profit with 1 stock.
        // 1 - most profit with no stock in cool down.
        // 2 - most profit with no stock not in cool down.
        let mut dp = vec![vec![0; 3]; n];

        dp[0][0] = 0 - prices[0];
        dp[0][1] = 0;
        dp[0][2] = 0;

        for i in 1..n {
            dp[i][0] = std::cmp::max(dp[i - 1][0], dp[i - 1][2] - prices[i]);
            dp[i][1] = dp[i - 1][0] + prices[i];
            dp[i][2] = std::cmp::max(dp[i - 1][1], dp[i - 1][2]);
        }
        println!("{:?}", dp);
        std::cmp::max(dp[n - 1][1], dp[n - 1][2])
    }
}

#[cfg(test)]
mod tests {
    use crate::best_time_to_buy_and_sell_stock_with_cooldown::Solution;
    #[test]
    fn case01() {
        let prices = vec![1, 2, 3, 0, 2];

        let actual = Solution::max_profit(prices);
        let expected = 3;
        assert_eq!(actual, expected);
    }
}
