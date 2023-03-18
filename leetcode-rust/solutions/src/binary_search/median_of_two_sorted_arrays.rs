// https://leetcode.com/problems/median-of-two-sorted-arrays/description/
struct Solution;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (n1, n2) = (nums1.len(), nums2.len());
        if n1 > n2 {
            return Solution::find_median_sorted_arrays(nums2, nums1);
        }
        let mut left = 0;
        let mut right = n1;
        while left <= right {
            let mid1 = (left + right) / 2;
            let mid2 = (n1 + n2 + 1) / 2 - mid1;
            let left1 = if mid1 == 0 { i32::MIN } else { nums1[mid1 - 1] };
            let right1 = if mid1 == n1 { i32::MAX } else { nums1[mid1] };
            let left2 = if mid2 == 0 { i32::MIN } else { nums2[mid2 - 1] };
            let right2 = if mid2 == n2 { i32::MAX } else { nums2[mid2] };
            if left1 <= right2 && left2 <= right1 {
                if (n1 + n2) % 2 == 0 {
                    return (left1.max(left2) as f64 + right1.min(right2) as f64) / 2.0;
                } else {
                    return left1.max(left2) as f64;
                }
            } else if left1 > right2 {
                right = mid1 - 1;
            } else {
                left = mid1 + 1;
            }
        }
        unreachable!();
    }
}

#[cfg(test)]
mod tests {
    use crate::binary_search::median_of_two_sorted_arrays::Solution;

    #[test]
    fn case01() {
        let nums1 = vec![1, 2];
        let nums2 = vec![3, 4];
        let actual = Solution::find_median_sorted_arrays(nums1, nums2);
        let expected = 2.5;
        assert_eq!(actual, expected);
    }
}