// https://leetcode.cn/problems/valid-palindrome/

struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s = s.chars().collect::<Vec<char>>();
        if s.is_empty() {
            return true;
        }
        let mut i = 0;
        let mut j = s.len() - 1;
        while i < j {
            if !s[i].is_ascii_alphanumeric() {
                i += 1;
                continue;
            }
            if !s[j].is_ascii_alphanumeric() {
                j -= 1;
                continue;
            }

            if s[i].to_ascii_lowercase() != s[j].to_ascii_lowercase() {
                return false;
            }

            i += 1;
            j -= 1;
        }
        true
    }
}

#[cfg(test)]
mod test {
    #[test]
    fn test01() {
        let s = "A man, a plan, a canal: Panama";
        assert_eq!(true, super::Solution::is_palindrome(s.to_string()));
    }

    #[test]
    fn test02() {
        let s = "race a car";
        assert_eq!(false, super::Solution::is_palindrome(s.to_string()));
    }

    #[test]
    fn test03() {
        let s = "  ";
        assert_eq!(true, super::Solution::is_palindrome(s.to_string()));
    }
}
