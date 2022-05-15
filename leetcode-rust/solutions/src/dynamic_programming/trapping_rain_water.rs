// https://leetcode-cn.com/problems/trapping-rain-water/

struct Solution;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() <= 2 {
            return 0;
        }
        let n = height.len();
        let mut max_left = vec![0; n];
        let mut max_right = vec![0; n];
        let mut ans = 0;

        max_left[0] = height[0];
        max_right[n - 1] = height[n - 1];

        for i in 1..n {
            max_left[i] = max_left[i - 1].max(height[i])
        }
        for i in (0..n - 1).rev() {
            max_right[i] = max_right[i + 1].max(height[i])
        }

        for i in 0..n {
            let tmp = max_left[i].min(max_right[i]) - height[i];
            if tmp > 0 {
                ans += tmp;
            }
        }

        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::dynamic_programming::trapping_rain_water::Solution;

    #[test]
    fn case01() {
        let height = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        let actual = Solution::trap(height);
        let expected = 6;
        assert_eq!(actual, expected)
    }
}
