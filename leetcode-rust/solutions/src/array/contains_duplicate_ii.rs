// https://leetcode.cn/problems/contains-duplicate-ii/

struct Solution;
impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut map = std::collections::HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            if let Some(j) = map.insert(num, i) {
                if (i - j) as i32 <= k {
                    return true;
                }
            }
        }
        false
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let nums = vec![1, 2, 3, 1];
        let k = 3;
        let expected = true;
        assert_eq!(expected, Solution::contains_nearby_duplicate(nums, k));
    }

    #[test]
    fn case02() {
        let nums = vec![1, 0, 1, 1];
        let k = 1;
        let expected = true;
        assert_eq!(expected, Solution::contains_nearby_duplicate(nums, k));
    }

    #[test]
    fn case03() {
        let nums = vec![1, 2, 3, 1, 2, 3];
        let k = 2;
        let expected = false;
        assert_eq!(expected, Solution::contains_nearby_duplicate(nums, k));
    }
}
