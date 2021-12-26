struct Solution;
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut r1 = 0;
        let mut r2;
        let mut r3 = 1;
        // let (mut r1, mut r2, mut r3) = (0, 0, 1);
        for _ in 1..n + 1 {
            r2 = r1;
            r1 = r3;
            r3 = r1 + r2;
        }
        r3
    }
}

#[cfg(test)]
mod tests {
    use crate::climbing_stairs::Solution;

    #[test]
    fn case01() {
        let actual = Solution::climb_stairs(4);
        let expected = 5;
        assert_eq!(actual, expected);
    }
}
