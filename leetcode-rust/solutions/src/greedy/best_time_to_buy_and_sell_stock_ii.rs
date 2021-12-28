// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in 1..prices.len() {
            ans += 0.max(prices[i] - prices[i - 1]);
        }
        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::best_time_to_buy_and_sell_stock_ii::Solution;

    #[test]
    fn case01() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        let actual = Solution::max_profit(prices);
        let expected = 7;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let prices = vec![1, 2, 3, 4, 5];
        let actual = Solution::max_profit(prices);
        let expected = 4;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let prices = vec![7, 6, 4, 3, 1];
        let actual = Solution::max_profit(prices);
        let expected = 0;
        assert_eq!(actual, expected);
    }
}