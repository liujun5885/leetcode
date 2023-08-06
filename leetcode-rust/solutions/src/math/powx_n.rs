// https://leetcode.cn/problems/powx-n/

pub struct Solution;

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        x.powi(n)
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let x = 2.00000;
        let n = 10;
        let expected = 1024.00000;
        let actual = Solution::my_pow(x, n);
        assert!(f64::abs(actual - expected) < 0.00001);
    }

    #[test]
    fn case2() {
        let x = 2.10000;
        let n = 3;
        let expected = 9.26100;
        let actual = Solution::my_pow(x, n);
        assert!(f64::abs(actual - expected) < 0.00001);
    }

    #[test]
    fn case3() {
        let x = 2.00000;
        let n = -2;
        let expected = 0.25000;
        let actual = Solution::my_pow(x, n);
        assert!(f64::abs(actual - expected) < 0.00001);
    }
}

