// https://leetcode-cn.com/problems/largest-number/


use std::cmp::Ordering;

struct Solution;

impl Solution {
    pub fn largest_number(nums: Vec<i32>) -> String {
        let mut num_str = nums.into_iter().map(
            |x| { x.to_string() }
        ).collect::<Vec<String>>();
        num_str.sort_by(
            |x1, x2| {
                let mut x1_chars = x1.clone();
                let mut x2_chars = x2.clone();

                while x1_chars.len() > 0 && x2_chars.len() > 0 {
                    let min_len = x1_chars.len().min(x2_chars.len());
                    let result = x2_chars[0..min_len].cmp(&x1_chars[0..min_len]);
                    if result != Ordering::Equal {
                        return result;
                    }

                    if x1_chars.len() > x2_chars.len() {
                        x1_chars = x1_chars[min_len..x1_chars.len()].to_string();
                    } else {
                        x2_chars = x2_chars[min_len..x2_chars.len()].to_string();
                    }
                }

                return Ordering::Equal;
            }
        );

        let ans = num_str.join("");
        if ans.as_bytes()[0] == '0' as u8 {
            return "0".to_string();
        } else {
            return ans;
        }
    }
}

#[cfg(test)]
mod test {
    use crate::sorting::largest_number::Solution;

    #[test]
    fn case01() {
        let nums = [10, 2].to_vec();
        let actual = Solution::largest_number(nums);
        let expected = "210".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let nums = [3, 30, 34, 5, 9].to_vec();
        let actual = Solution::largest_number(nums);
        let expected = "9534330".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let nums = [111311, 1113].to_vec();
        let actual = Solution::largest_number(nums);
        let expected = "1113111311".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let nums = [432, 43243].to_vec();
        let actual = Solution::largest_number(nums);
        let expected = "43243432".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case05() {
        let nums = [0, 0].to_vec();
        let actual = Solution::largest_number(nums);
        let expected = "0".to_string();
        assert_eq!(actual, expected);
    }
}