// https://leetcode.cn/problems/plus-one/

struct Solution;

impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut result = digits.clone();
        let mut i = result.len() - 1;
        loop {
            if result[i] == 9 {
                result[i] = 0;
                if i == 0 {
                    result.insert(0, 1);
                    break;
                }
                i -= 1;
            } else {
                result[i] += 1;
                break;
            }
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn case1() {
        let digits = vec![1, 2, 3];
        let expected = vec![1, 2, 4];
        let actual = Solution::plus_one(digits);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case2() {
        let digits = vec![4, 3, 2, 1];
        let expected = vec![4, 3, 2, 2];
        let actual = Solution::plus_one(digits);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case3() {
        let digits = vec![0];
        let expected = vec![1];
        let actual = Solution::plus_one(digits);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case4() {
        let digits = vec![9];
        let expected = vec![1, 0];
        let actual = Solution::plus_one(digits);
        assert_eq!(actual, expected);
    }
}
