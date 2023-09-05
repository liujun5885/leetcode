// https://leetcode.cn/problems/excel-sheet-column-number/

struct Solution;
impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        let mut result = 0;
        for c in column_title.chars() {
            result = result * 26 + (c as u8 - 'A' as u8 + 1) as i32;
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let column_title = "A".to_string();
        let expected = 1;
        assert_eq!(expected, Solution::title_to_number(column_title));
    }

    #[test]
    fn case02() {
        let column_title = "AB".to_string();
        let expected = 28;
        assert_eq!(expected, Solution::title_to_number(column_title));
    }

    #[test]
    fn case03() {
        let column_title = "ZY".to_string();
        let expected = 701;
        assert_eq!(expected, Solution::title_to_number(column_title));
    }

    #[test]
    fn case04() {
        let column_title = "FXSHRXW".to_string();
        let expected = 2147483647;
        assert_eq!(expected, Solution::title_to_number(column_title));
    }
}
