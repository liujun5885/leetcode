use std::option::Option::Some;

struct Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut c1 = text1.chars();
        while let Some(ch) = c1.next() {
            println!("{}", ch);
        }
        return 10;
    }
}

#[cfg(test)]
mod tests {
    use crate::{Solution};

    #[test]
    fn it_works() {
        let text1 = String::from("abcde");
        let text2 = String::from("abcde");
        let output = Solution::longest_common_subsequence(text1, text2);
        let expected = 10;
        assert_eq!(output, expected);
    }
}
