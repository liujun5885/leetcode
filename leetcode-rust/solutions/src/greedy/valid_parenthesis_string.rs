// https://leetcode-cn.com/problems/valid-parenthesis-string/

struct Solution;

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let (mut min_count, mut max_count) = (0, 0);

        for c in s.chars() {
            if c == '(' {
                min_count += 1;
                max_count += 1;
            } else if c == ')' {
                min_count = 0.max(min_count - 1);
                max_count -= 1;
                if max_count < 0 {
                    return false;
                }
            } else {
                min_count = 0.max(min_count - 1);
                max_count += 1
            }
        }

        return min_count == 0;
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::valid_parenthesis_string::Solution;

    #[test]
    fn case01() {
        let s = "()".to_string();
        let actual = Solution::check_valid_string(s);
        let expected = true;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let s = "(*)".to_string();
        let actual = Solution::check_valid_string(s);
        let expected = true;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let s = "(*))".to_string();
        let actual = Solution::check_valid_string(s);
        let expected = true;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let s = "(*)))".to_string();
        let actual = Solution::check_valid_string(s);
        let expected = false;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case05() {
        let s = "()(((*)".to_string();
        let actual = Solution::check_valid_string(s);
        let expected = false;
        assert_eq!(actual, expected);
    }
}
