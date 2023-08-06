struct Solution;

impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        dividend / divisor
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let dividend = 10;
        let divisor = 3;
        let expected = 3;
        let actual = Solution::divide(dividend, divisor);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case2() {
        let dividend = 7;
        let divisor = -3;
        let expected = -2;
        let actual = Solution::divide(dividend, divisor);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case3() {
        let dividend = 2147483647;
        let divisor = 1;
        let expected = 2147483647;
        let actual = Solution::divide(dividend, divisor);
        assert_eq!(actual, expected);
    }
}
