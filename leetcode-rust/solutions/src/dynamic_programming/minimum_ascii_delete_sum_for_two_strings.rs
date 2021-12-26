// https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/

struct Solution;

impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let c1 = s1.as_bytes();
        let c2 = s2.as_bytes();

        let mut dp = vec![vec![0; s2.len() + 1]; s1.len() + 1];

        for i in 1..=s1.len() {
            dp[i][0] = dp[i - 1][0] + c1[i - 1] as i32;
        }
        for j in 1..=s2.len() {
            dp[0][j] = dp[0][j - 1] + c2[j - 1] as i32;
        }

        for i in 1..=s1.len() {
            for j in 1..=s2.len() {
                if c1[i - 1] != c2[j - 1] {
                    dp[i][j] = std::cmp::min(
                        dp[i - 1][j - 1] + c1[i - 1] as i32 + c2[j - 1] as i32,
                        dp[i - 1][j] + c1[i - 1] as i32,
                    )
                    .min(dp[i][j - 1] + c2[j - 1] as i32);
                } else {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }

        println!("{:?}", dp);
        dp[s1.len()][s2.len()]
    }
}

#[cfg(test)]
mod tests {
    use crate::minimum_ascii_delete_sum_for_two_strings::Solution;
    #[test]
    fn case01() {
        let s1 = "sea".to_string();
        let s2 = "eat".to_string();
        let actual = Solution::minimum_delete_sum(s1, s2);
        let expected = 231;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let s1 = "delete".to_string();
        let s2 = "leet".to_string();
        let actual = Solution::minimum_delete_sum(s1, s2);
        let expected = 403;
        assert_eq!(actual, expected);
    }
}
