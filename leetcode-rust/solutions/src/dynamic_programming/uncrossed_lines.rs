// https://leetcode-cn.com/problems/uncrossed-lines/
struct Solution;
impl Solution {
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let m = nums1.len();
        let n = nums2.len();
        let mut dp = vec![vec![0; n + 1]; m + 1];

        for i in 1..m + 1 {
            for j in 1..n + 1 {
                if nums1[i - 1] == nums2[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1
                } else {
                    dp[i][j] = dp[i][j - 1].max(dp[i - 1][j]);
                }
            }
        }

        dp[m][n]
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::uncrossed_lines::Solution;
    #[test]
    fn case01() {
        let nums1 = vec![1, 4, 2];
        let nums2 = vec![1, 2, 4];
        let expected = 2;
        let acutal = Solution::max_uncrossed_lines(nums1, nums2);
        assert_eq!(acutal, expected);
    }
}
