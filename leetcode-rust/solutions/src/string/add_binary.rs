// https://leetcode.cn/problems/add-binary/

struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let a_rev: Vec<char> = a.chars().rev().collect();
        let b_rev: Vec<char> = b.chars().rev().collect();
        let mut result = String::new();
        let mut i = 0;
        let mut carry = 0;
        loop {
            let mut sum = carry;
            if i < a_rev.len() {
                sum += a_rev[i].to_digit(10).unwrap();
            }
            if i < b_rev.len() {
                sum += b_rev[i].to_digit(10).unwrap();
            }
            if sum == 0 && i >= a_rev.len() && i >= b_rev.len() {
                break;
            }
            carry = sum / 2;
            result.push_str(&(sum % 2).to_string());
            i += 1;
        }
        result.chars().rev().collect()
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let a = "11".to_string();
        let b = "1".to_string();
        let expected = "100".to_string();
        let actual = Solution::add_binary(a, b);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case2() {
        let a = "1010".to_string();
        let b = "1011".to_string();
        let expected = "10101".to_string();
        let actual = Solution::add_binary(a, b);
        assert_eq!(actual, expected);
    }
}
