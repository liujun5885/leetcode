struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut start = 0;
        let mut end = n as i32 - 1;

        while start <= end {
            let cur = (start + end) / 2;
            if nums[cur as usize] < target {
                start = cur + 1;
            } else if nums[cur as usize] > target {
                end = cur - 1;
            } else {
                return cur as i32;
            }
        }
        return -1;
    }
}

#[cfg(test)]
mod tests {
    use crate::array::binary_search::Solution;

    #[test]
    fn case01() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 2;
        let expected = -1;
        let actual = Solution::search(nums, target);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 9;
        let expected = 4;
        let actual = Solution::search(nums, target);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let nums = vec![5];
        let target = -5;
        let expected = -1;
        let actual = Solution::search(nums, target);
        assert_eq!(actual, expected);
    }
}