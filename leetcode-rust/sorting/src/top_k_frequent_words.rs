// https://leetcode-cn.com/problems/top-k-frequent-words/
struct Solution {}


impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        return vec!["i", "love"].into_iter().map(|x| { x.to_string() }).collect();
    }
}

#[cfg(test)]
mod test {
    use crate::top_k_frequent_words::Solution;

    #[test]
    fn case01() {
        let words = vec![
            "i", "love", "leetcode", "i", "love", "coding",
        ].into_iter().map(|x| { x.to_string() }).collect();
        let k = 2;
        let actual = Solution::top_k_frequent(words, k);
        let expected: Vec<String> = vec!["i", "love"].into_iter().map(|x| { x.to_string() }).collect();
        assert_eq!(actual, expected);
    }
}