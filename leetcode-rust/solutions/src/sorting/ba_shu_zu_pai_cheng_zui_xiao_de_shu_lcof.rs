// https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/

use std::cmp::Ordering;

struct Solution;

impl Solution {
    pub fn min_number(nums: Vec<i32>) -> String {
        let mut num_str = nums.into_iter().map(
            |x| { x.to_string() }
        ).collect::<Vec<String>>();
        num_str.sort_by(
            |x1, x2| {
                let mut x1_chars = x1.clone();
                let mut x2_chars = x2.clone();

                while x1_chars.len() > 0 && x2_chars.len() > 0 {
                    let min_len = x1_chars.len().min(x2_chars.len());
                    let result = x1_chars[0..min_len].cmp(&x2_chars[0..min_len]);
                    if result != Ordering::Equal {
                        return result;
                    }

                    if x1_chars.len() > x2_chars.len() {
                        x1_chars = x1_chars[min_len..x1_chars.len()].to_string();
                    } else {
                        x2_chars = x2_chars[min_len..x2_chars.len()].to_string();
                    }
                }

                return Ordering::Equal;
            }
        );

        return num_str.join("");

        // let ans = num_str.join("");
        // let mut not_zero_index = 0 as i32;
        // for i in 0..ans.len() {
        //     if ans.chars().nth(i).unwrap() == '0' {
        //         not_zero_index += 1;
        //     } else {
        //         break
        //     }
        // }
        //
        // return ans[0.max(not_zero_index - 1) as usize..].to_string();
    }
}

#[cfg(test)]
mod test {
    use crate::sorting::ba_shu_zu_pai_cheng_zui_xiao_de_shu_lcof::Solution;

    #[test]
    fn case01() {
        let num = [10, 2].to_vec();

        let actual = Solution::min_number(num);
        let expected = "102".to_string();

        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let num = [0, 0].to_vec();

        let actual = Solution::min_number(num);
        let expected = "0".to_string();

        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0].to_vec();

        let actual = Solution::min_number(num);
        let expected = "0123456789".to_string();

        assert_eq!(actual, expected);
    }

    #[test]
    fn case04() {
        let num = [1].to_vec();

        let actual = Solution::min_number(num);
        let expected = "1".to_string();

        assert_eq!(actual, expected);
    }
}