// https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit = 0;
        let mut lowest = i32::MAX;

        for p in prices {
            lowest = std::cmp::min(lowest, p);
            profit = std::cmp::max(profit, p - lowest);
        }

        profit
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::best_time_to_buy_and_sell_stock::Solution;
    #[test]
    fn case01() {
        let prices = vec![7, 1, 5, 3, 6, 4];
        let actual = Solution::max_profit(prices);
        let expected = 5;
        assert_eq!(actual, expected);
    }
    #[test]
    fn case02() {
        let prices = vec![7, 6, 4, 3, 1];
        let actual = Solution::max_profit(prices);
        let expected = 0;
        assert_eq!(actual, expected);
    }
}
