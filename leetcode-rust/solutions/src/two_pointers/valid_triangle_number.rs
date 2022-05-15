// https://leetcode-cn.com/problems/valid-triangle-number/

struct Solution;

impl Solution {
    pub fn triangle_number(nums: Vec<i32>) -> i32 {
        let mut sorted_nums = nums.clone();
        sorted_nums.sort();
        let mut ans = 0;

        for i in 0..sorted_nums.len() {
            let mut k = i;
            for j in i + 1..sorted_nums.len() {
                while k + 1 < sorted_nums.len()
                    && sorted_nums[i] + sorted_nums[j] > sorted_nums[k + 1]
                {
                    k += 1;
                }
                ans += 0.max(k as i32 - j as i32);
            }
        }

        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::two_pointers::valid_triangle_number::Solution;

    #[test]
    fn case01() {
        let nums = vec![2, 2, 3, 4];
        let actual = Solution::triangle_number(nums);
        let expected = 3;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let nums = vec![4, 2, 3, 4];
        let actual = Solution::triangle_number(nums);
        let expected = 4;
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let nums = vec![0, 0, 0];
        let actual = Solution::triangle_number(nums);
        let expected = 0;
        assert_eq!(actual, expected);
    }
}
