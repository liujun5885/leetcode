// https://leetcode-cn.com/problems/heaters/

struct Solution;

impl Solution {
    pub fn find_radius(houses: Vec<i32>, heaters: Vec<i32>) -> i32 {
        1
    }
}

#[cfg(test)]
mod tests {
    use crate::binary_search::heaters::Solution;

    #[test]
    fn case01() {
        let houses = vec![1, 2, 3];
        let heaters = vec![2];
        let actual = Solution::find_radius(houses, heaters);
        let expected = 1;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let houses = vec![1, 2, 3, 4];
        let heaters = vec![1, 4];
        let actual = Solution::find_radius(houses, heaters);
        let expected = 1;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let houses = vec![1, 5];
        let heaters = vec![2];
        let actual = Solution::find_radius(houses, heaters);
        let expected = 3;
        assert_eq!(actual, expected);
    }
}