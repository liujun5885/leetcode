// https://leetcode-cn.com/problems/unique-binary-search-trees/
struct Solution;

impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        let mut dp = vec![0; n as usize + 1];
        dp[0] = 1;
        dp[1] = 1;

        for i in 2..=n as usize {
            for j in 1..=i {
                dp[i] += dp[j - 1] * dp[i - j]
            }
        }

        return dp[n as usize];
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::unique_binary_search_trees::Solution;

    #[test]
    fn case01() {
        let n = 3;
        let expected = 5;
        let actual = Solution::num_trees(n);
        assert_eq!(actual, expected)
    }
}