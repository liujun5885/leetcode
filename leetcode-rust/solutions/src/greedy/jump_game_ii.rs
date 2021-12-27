// https://leetcode-cn.com/problems/jump-game-ii/

struct Solution;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut steps = 0;
        let mut max_position = 0;
        let mut end = 0;

        for i in 0..nums.len() - 1 {
            let tmp = i as i32;
            max_position = max_position.max(tmp + nums[i]);
            if end == tmp {
                steps += 1;
                end = max_position;
            }
        }

        return steps;
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::jump_game_ii::Solution;

    #[test]
    fn case01() {
        let nums = vec![2, 3, 1, 1, 4];
        let actual = Solution::jump(nums);
        let expected = 2;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let nums = vec![2, 3, 0, 1, 4];
        let actual = Solution::jump(nums);
        let expected = 2;
        assert_eq!(actual, expected);
    }
}