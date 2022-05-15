// https://leetcode-cn.com/problems/boats-to-save-people/

struct Solution;

impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 {
        let mut sorted_people = people.clone();
        let mut ans = 0;
        sorted_people.sort();
        let mut light = 0;
        let mut heavy = sorted_people.len() - 1;

        while light < heavy {
            if sorted_people[heavy] > limit {
                return 0;
            }
            if sorted_people[heavy] + sorted_people[light] > limit {
                heavy -= 1;
            } else {
                light += 1;
                heavy -= 1;
            }
            ans += 1;
        }
        if light == heavy {
            ans += 1;
        }

        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::boats_to_save_people::Solution;

    #[test]
    fn case01() {
        let people = vec![1, 2];
        let limit = 3;
        let actual = Solution::num_rescue_boats(people, limit);
        let expected = 1;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let people = vec![3, 2, 2, 1];
        let limit = 3;
        let actual = Solution::num_rescue_boats(people, limit);
        let expected = 3;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let people = vec![3, 5, 3, 4];
        let limit = 5;
        let actual = Solution::num_rescue_boats(people, limit);
        let expected = 4;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let people = vec![1, 2, 3, 4];
        let limit = 5;
        let actual = Solution::num_rescue_boats(people, limit);
        let expected = 2;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case05() {
        let people = vec![1, 2, 3, 4, 5];
        let limit = 6;
        let actual = Solution::num_rescue_boats(people, limit);
        let expected = 3;
        assert_eq!(actual, expected);
    }
}
