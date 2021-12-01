// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let n = prices.len();
        let mut dp = vec![vec![0; 2]; n];

        dp[0][0] = 0;
        dp[0][1] = 0 - prices[0];

        for i in 1..n {
            dp[i][0] = std::cmp::max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee);
            dp[i][1] = std::cmp::max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }

        dp[n - 1][0]
    }
}

#[cfg(test)]
mod tests {
    use crate::best_time_to_buy_and_sell_stock_with_transaction_fee::Solution;
    #[test]
    fn case01() {
        let prices = vec![1, 3, 2, 8, 4, 9];
        let fee = 2;
        let actual = Solution::max_profit(prices, fee);
        let expected = 8;
        assert_eq!(actual, expected);
    }
}
