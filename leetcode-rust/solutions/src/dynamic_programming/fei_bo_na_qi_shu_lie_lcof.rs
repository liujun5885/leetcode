// https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/submissions/

struct Solution;

impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n < 1 {
            return 0;
        }
        if n == 1 {
            return 1;
        }
        let mut dp = vec![0; n as usize + 1];
        dp[0] = 0;
        dp[1] = 1;

        for i in 2..=n as usize {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        }
        return dp[n as usize];
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::fei_bo_na_qi_shu_lie_lcof::Solution;

    #[test]
    fn case01() {
        let n = 2;
        let expected = 1;
        let actual = Solution::fib(n);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let n = 5;
        let expected = 5;
        let actual = Solution::fib(n);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let n = 48;
        let expected = 807526948;
        let actual = Solution::fib(n);
        assert_eq!(actual, expected);
    }
}
