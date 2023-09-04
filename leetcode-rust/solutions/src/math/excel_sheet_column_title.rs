// https://leetcode.cn/problems/excel-sheet-column-title/

struct Solution;
impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let mut result = vec![];
        let mut n = column_number;
        while n > 0 {
            result.push((((n - 1) % 26) as u8 + 'A' as u8) as char);
            n = (n - 1) / 26;
        }
        result.reverse();
        result.iter().collect::<String>()
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let column_number = 1;
        let expected = "A".to_string();
        assert_eq!(expected, Solution::convert_to_title(column_number));
    }

    #[test]
    fn case02() {
        let column_number = 28;
        let expected = "AB".to_string();
        assert_eq!(expected, Solution::convert_to_title(column_number));
    }

    #[test]
    fn case03() {
        let column_number = 701;
        let expected = "ZY".to_string();
        assert_eq!(expected, Solution::convert_to_title(column_number));
    }

    #[test]
    fn case04() {
        let column_number = 2147483647;
        let expected = "FXSHRXW".to_string();
        assert_eq!(expected, Solution::convert_to_title(column_number));
    }
}
