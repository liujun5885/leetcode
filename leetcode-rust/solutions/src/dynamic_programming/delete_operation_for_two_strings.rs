// https://leetcode-cn.com/problems/delete-operation-for-two-strings/

#[allow(dead_code)]
struct Solution;

impl Solution {
    #[allow(dead_code)]
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let len1 = word1.len();
        let len2 = word2.len();
        let mut dp = vec![vec![0; len2 + 1]; len1 + 1];

        for i in 1..=len1 {
            dp[i][0] = i;
        }
        for j in 1..=len2 {
            dp[0][j] = j;
        }

        for i in 1..=len1 {
            for j in 1..=len2 {
                if word1.as_bytes()[i - 1] == word2.as_bytes()[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = dp[i][j - 1].min(dp[i - 1][j]) + 1;
                }
            }
        }

        return dp[len1][len2] as i32;
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::delete_operation_for_two_strings::Solution;

    #[test]
    fn case01() {
        let word1 = "sea".to_string();
        let word2 = "eat".to_string();
        let expected = 2;
        let actual = Solution::min_distance(word1, word2);
        assert_eq!(actual, expected)
    }

    #[test]
    fn case02() {
        let word1 = "leetcode".to_string();
        let word2 = "etco".to_string();
        let expected = 4;
        let actual = Solution::min_distance(word1, word2);
        assert_eq!(actual, expected)
    }

    #[test]
    fn case03() {
        let word1 = "a".to_string();
        let word2 = "a".to_string();
        let expected = 0;
        let actual = Solution::min_distance(word1, word2);
        assert_eq!(actual, expected)
    }

    #[test]
    fn case04() {
        let word1 = "a".to_string();
        let word2 = "b".to_string();
        let expected = 2;
        let actual = Solution::min_distance(word1, word2);
        assert_eq!(actual, expected)
    }
}
