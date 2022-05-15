// https://leetcode-cn.com/problems/remove-duplicate-letters/

struct Solution;

impl Solution {
    pub fn remove_duplicate_letters(s: String) -> String {
        let mut char_counter = vec![0; 26];
        let mut visited = vec![false; 26];

        for c in s.chars() {
            let i = c as usize - 'a' as usize;
            char_counter[i] += 1
        }

        let mut ans: Vec<char> = vec![];

        for c in s.chars() {
            while !ans.is_empty() && ans.last().unwrap() > &c {
                let last = *ans.last().unwrap();
                if char_counter[(last as u8 - 'a' as u8) as usize] <= 0
                    || visited[(c as u8 - 'a' as u8) as usize]
                {
                    break;
                }
                ans.pop();
                visited[(last as u8 - 'a' as u8) as usize] = false;
            }
            if visited[(c as u8 - 'a' as u8) as usize] == false {
                ans.push(c);
                visited[(c as u8 - 'a' as u8) as usize] = true;
            }
            char_counter[(c as u8 - 'a' as u8) as usize] -= 1;
        }

        return ans.into_iter().collect();
    }
}

#[cfg(test)]
mod test {
    use crate::greedy::remove_duplicate_letters::Solution;

    #[test]
    fn case01() {
        let s = "bcabc";
        let actual = Solution::remove_duplicate_letters(s.to_string());
        let expected = "abc".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let s = "cbacdcbc";
        let actual = Solution::remove_duplicate_letters(s.to_string());
        let expected = "acdb".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case03() {
        let s = "abacb";
        let actual = Solution::remove_duplicate_letters(s.to_string());
        let expected = "abc".to_string();
        assert_eq!(actual, expected);
    }
}
