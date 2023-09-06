// https://leetcode.cn/problems/power-of-two/

struct Solution;
impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        if n <= 0 {
            return false;
        }

        n & (n - 1) == 0
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let n = 1;
        let expected = true;
        assert_eq!(expected, Solution::is_power_of_two(n));
    }

    #[test]
    fn case02() {
        let n = 16;
        let expected = true;
        assert_eq!(expected, Solution::is_power_of_two(n));
    }

    #[test]
    fn case03() {
        let n = 3;
        let expected = false;
        assert_eq!(expected, Solution::is_power_of_two(n));
    }

    #[test]
    fn case04() {
        let n = 4;
        let expected = true;
        assert_eq!(expected, Solution::is_power_of_two(n));
    }

    #[test]
    fn case05() {
        let n = 5;
        let expected = false;
        assert_eq!(expected, Solution::is_power_of_two(n));
    }
}
