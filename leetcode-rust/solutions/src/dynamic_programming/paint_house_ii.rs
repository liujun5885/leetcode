// https://leetcode-cn.com/problems/paint-house-ii/

struct Solution;

impl Solution {
    pub fn min_cost_ii(costs: Vec<Vec<i32>>) -> i32 {
        let k = costs[0].len();
        let n = costs.len();
        let mut dp = vec![vec![0; k]; n + 1];
        let mut min1 = 0;
        let mut min2 = 1;

        for i in 1..n + 1 {
            let mut a1 = i32::MAX;
            let mut a2 = i32::MAX;
            let (mut i1, mut i2) = (0, 0);
            for j in 0..k {
                if j == min1 {
                    dp[i][j] = dp[i - 1][min2] + costs[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][min1] + costs[i - 1][j];
                }
                if dp[i][j] < a1 {
                    i2 = i1;
                    a2 = a1;
                    i1 = j;
                    a1 = dp[i][j];
                } else if dp[i][j] < a2 {
                    i2 = j;
                    a2 = dp[i][j];
                }
            }
            min1 = i1;
            min2 = i2;
        }

        *dp[n].iter().min().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::paint_house_ii::Solution;
    #[test]
    fn case01() {
        let raw = [[1, 5, 3], [2, 9, 4]];
        let mut costs = Vec::new();
        for i in raw.iter() {
            let mut tmp = Vec::new();
            for j in i.iter() {
                tmp.push(*j);
            }
            costs.push(tmp);
        }
        let actual = Solution::min_cost_ii(costs);
        let expected = 5;
        assert_eq!(actual, expected);
    }
}
