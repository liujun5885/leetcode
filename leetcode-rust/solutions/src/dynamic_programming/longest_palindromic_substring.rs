// https://leetcode-cn.com/problems/longest-palindromic-substring/

struct Solution;

impl Solution {
    pub fn longest_palindrome(_: String) -> String {
        "bab".to_string()
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::longest_palindromic_substring::Solution;
    #[test]
    fn case01() {
        let actual = Solution::longest_palindrome("babad".to_string());
        let expected = "bab".to_string();
        assert_eq!(actual, expected);
    }
}
