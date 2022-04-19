// https://leetcode-cn.com/problems/heaters/

use bisection;

struct Solution;

impl Solution {
    pub fn find_radius(houses: Vec<i32>, heaters: Vec<i32>) -> i32 {
        let mut sorted_heaters = heaters.clone();
        sorted_heaters.sort();
        let mut ans = 0;

        for house in houses {
            let j = bisection::bisect_left(&sorted_heaters, &house);
            let i = j as i32 - 1;
            let right_diff = if j >= heaters.len() { i32::MAX - house } else { sorted_heaters[j] - house };
            let left_diff = if i < 0 { i32::MAX - house } else { house - sorted_heaters[i as usize] };
            ans = right_diff.min(left_diff).max(ans);
        }

        return ans;
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