use std::cmp;

struct Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let char1 = text1.as_bytes();
        let char2 = text2.as_bytes();
        let m = text1.len();
        let n = text2.len();
        let mut dp = vec![vec![0; n + 1]; m + 1];
        for i in 1..m + 1 {
            for j in 1..n + 1 {
                if char1[i - 1] == char2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = cmp::max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        dp[m][n]
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::longest_common_subsequence::Solution;

    #[test]
    fn case01() {
        let text1 = String::from("baaaccee");
        let text2 = String::from("ace");
        let actual = Solution::longest_common_subsequence(text1, text2);
        let expected = 3;
        assert_eq!(actual, expected);
    }
}
