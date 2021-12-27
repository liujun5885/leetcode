struct Solution;

impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut max_position = 0;

        for i in 0..nums.len() {
            if max_position >= i && i + nums[i] as usize > max_position {
                max_position = i + nums[i] as usize;
            } else if max_position < i {
                return false;
            }
        }

        return true;
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::jump_game::Solution;

    #[test]
    fn case01() {
        let nums = vec![2, 3, 1, 1, 4];
        let actual = Solution::can_jump(nums);
        let expected = true;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let nums = vec![3, 2, 1, 0, 4];
        let actual = Solution::can_jump(nums);
        let expected = false;
        assert_eq!(actual, expected);
    }
}