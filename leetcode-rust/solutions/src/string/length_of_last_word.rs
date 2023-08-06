// https://leetcode.cn/problems/length-of-last-word/

struct Solution;

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut result = 0;

        for i in s.split(" ") {
            if i.len() > 0 {
                result = i.len();
            }
        }
        result as i32
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let s = "Hello World".to_string();
        let expected = 5;
        let actual = Solution::length_of_last_word(s);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case2() {
        let s = " ".to_string();
        let expected = 0;
        let actual = Solution::length_of_last_word(s);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case3() {
        let s = "   fly me   to   the moon  ".to_string();
        let expected = 4;
        let actual = Solution::length_of_last_word(s);
        assert_eq!(actual, expected);
    }
}
