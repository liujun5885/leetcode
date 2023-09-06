// https://leetcode.cn/problems/summary-ranges/

struct Solution;

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut result = vec![];
        if nums.len() == 0 {
            return result;
        }

        let mut start = 0;
        let mut end = 0;

        for i in 1..nums.len() {
            if nums[i] == nums[i - 1] + 1 {
                end += 1;
            } else {
                if start == end {
                    result.push(nums[start].to_string());
                } else {
                    result.push(format!("{}->{}", nums[start], nums[end]));
                }
                start = i;
                end = i;
            }
        }

        if start == end {
            result.push(nums[start].to_string());
        } else {
            result.push(format!("{}->{}", nums[start], nums[end]));
        }

        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let nums = vec![0, 1, 2, 4, 5, 7];
        let expected = vec!["0->2".to_string(), "4->5".to_string(), "7".to_string()];
        assert_eq!(expected, Solution::summary_ranges(nums));
    }

    #[test]
    fn case02() {
        let nums = vec![0, 2, 3, 4, 6, 8, 9];
        let expected = vec![
            "0".to_string(),
            "2->4".to_string(),
            "6".to_string(),
            "8->9".to_string(),
        ];
        assert_eq!(expected, Solution::summary_ranges(nums));
    }

    #[test]
    fn case03() {
        let nums = vec![];
        let expected: Vec<String> = vec![];
        assert_eq!(expected, Solution::summary_ranges(nums));
    }

    #[test]
    fn case04() {
        let nums = vec![-1];
        let expected = vec!["-1".to_string()];
        assert_eq!(expected, Solution::summary_ranges(nums));
    }

    #[test]
    fn case05() {
        let nums = vec![0];
        let expected = vec!["0".to_string()];
        assert_eq!(expected, Solution::summary_ranges(nums));
    }
}
