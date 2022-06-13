struct Solution;

impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 { return 0; }
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
}
