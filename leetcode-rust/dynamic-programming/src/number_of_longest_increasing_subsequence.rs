// https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

struct Solution;
impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![1; nums.len()];
        let mut max_counter = vec![0; nums.len() + 1];
        let mut max_num = 1;

        // 长度是1的字串，至少有一个
        max_counter[1] = 1;

        for i in 1..nums.len() {
            for j in 0..i {
                if nums[j] < nums[i] {
                    dp[i] = dp[i].max(dp[j] + 1);
                }
            }
            if dp[i] >= max_num {
                max_counter[max_num] += 1;
                max_num = dp[i];
            }
        }

        println!("{:?}", max_num);
        println!("{:?}", dp);
        println!("{:?}", max_counter);

        max_counter[max_num] as i32
    }
}

#[cfg(test)]
mod tests {
    use crate::number_of_longest_increasing_subsequence::Solution;
    // #[test]
    // fn case01() {
    //     let nums = vec![1, 3, 5, 4, 7];
    //     let actual = Solution::find_number_of_lis(nums);
    //     let expected = 2;
    //     assert_eq!(actual, expected)
    // }

    #[test]
    fn case02() {
        let nums = vec![2, 2, 2, 2, 2];
        let actual = Solution::find_number_of_lis(nums);
        let expected = 5;
        assert_eq!(actual, expected)
    }

    // #[test]
    // fn case03() {
    //     let nums = vec![1, 2, 4, 3, 5, 4, 7, 2];
    //     let actual = Solution::find_number_of_lis(nums);
    //     let expected = 3;
    //     assert_eq!(actual, expected)
    // }
}
