// https://leetcode-cn.com/problems/generate-parentheses/

struct Solution;

impl Solution {
    fn backtrace(
        result: &mut Vec<String>,
        buf: &mut Vec<char>,
        cur: usize,
        n: usize,
        left_num: usize,
        right_num: usize,
    ) {
        if cur == 2 * n {
            let s = buf.iter().cloned().collect::<String>();
            result.push(s);
            return;
        }
        if left_num < n {
            buf[cur] = '(';
            Solution::backtrace(result, buf, cur + 1, n, left_num + 1, right_num);
            buf[cur] = '-';
        }
        if right_num < left_num {
            buf[cur] = ')';
            Solution::backtrace(result, buf, cur + 1, n, left_num, right_num + 1);
            buf[cur] = '-';
        }
    }
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut buf = vec!['-'; 2 * n as usize];
        Solution::backtrace(&mut result, &mut buf, 0, n as usize, 0, 0);
        result
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::generate_parentheses::Solution;

    #[test]
    fn case01() {
        let actual = Solution::generate_parenthesis(3);
        let expected = vec!["((()))", "(()())", "(())()", "()(())", "()()()"];
        assert_eq!(actual, expected);
    }
}
