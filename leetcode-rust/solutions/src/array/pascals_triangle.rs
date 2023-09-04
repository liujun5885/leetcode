// https://leetcode.cn/problems/pascals-triangle/

struct Solution;

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];

        for i in 0..num_rows as usize {
            let mut row = vec![1; i + 1];
            for j in 1..i {
                row[j] = result[i - 1][j - 1] + result[i - 1][j];
            }
            result.push(row);
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let num_rows = 5;
        let expected = vec![
            vec![1],
            vec![1, 1],
            vec![1, 2, 1],
            vec![1, 3, 3, 1],
            vec![1, 4, 6, 4, 1],
        ];
        assert_eq!(expected, Solution::generate(num_rows));
    }

    #[test]
    fn case02() {
        let num_rows = 1;
        let expected = vec![vec![1]];
        assert_eq!(expected, Solution::generate(num_rows));
    }
}
