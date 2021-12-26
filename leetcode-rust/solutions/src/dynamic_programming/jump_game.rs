// https://leetcode-cn.com/problems/jump-game/

struct Solution;

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        println!("{:?}", nums);
        true
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::jump_game::Solution;

    #[test]
    fn case01() {
        let nums = vec![2, 3, 1, 1, 4];
        let actual = Solution::can_jump(nums);
        let expected = true;
        assert_eq!(actual, expected);
    }
}
