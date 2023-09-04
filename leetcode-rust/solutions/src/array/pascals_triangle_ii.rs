// https://leetcode.cn/problems/pascals-triangle-ii/

struct Solution;
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut result: Vec<Vec<i32>> = vec![];

        for i in 0..row_index as usize + 1 {
            let mut row = vec![1; i + 1];
            for j in 1..i {
                row[j] = result[i - 1][j - 1] + result[i - 1][j];
            }
            result.push(row);
        }
        result.pop().unwrap()
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let row_index = 3;
        let expected = vec![1, 3, 3, 1];
        assert_eq!(expected, Solution::get_row(row_index));
    }

    #[test]
    fn case02() {
        let row_index = 0;
        let expected = vec![1];
        assert_eq!(expected, Solution::get_row(row_index));
    }

    #[test]
    fn case03() {
        let row_index = 1;
        let expected = vec![1, 1];
        assert_eq!(expected, Solution::get_row(row_index));
    }
}
