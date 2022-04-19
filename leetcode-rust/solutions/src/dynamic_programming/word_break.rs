// https://leetcode-cn.com/problems/word-break/

use std::collections::{HashSet};

struct Solution {}

impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut dp = vec![false; s.len() + 1];
        let mut str_set = HashSet::new();

        for i in word_dict.iter() {
            str_set.insert(i);
        }

        dp[0] = true;
        for i in 1..=s.len() {
            for j in 0..i {
                if dp[j] && str_set.contains(&s[j..i].to_string()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.len()];
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::word_break::Solution;

    #[test]
    fn case01() {
        let s = "leetcode";
        let word_dict = ["leet", "code"].iter().map(|x| { String::from(*x) }).collect();
        let actual = Solution::word_break(s.to_string(), word_dict);
        let expected = true;
        assert_eq!(actual, expected);
    }
}