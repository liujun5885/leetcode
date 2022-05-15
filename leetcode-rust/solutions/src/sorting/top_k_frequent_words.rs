// https://leetcode-cn.com/problems/top-k-frequent-words/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        let mut word_counter = HashMap::new();
        for word in words.iter() {
            word_counter.insert(String::from(word), word_counter.get(word).unwrap_or(&0) + 1);
        }

        let mut n_vs_word = word_counter
            .into_iter()
            .map(|x| (x.1, x.0))
            .collect::<Vec<_>>();
        n_vs_word.sort_by(|x1, x2| x1.0.cmp(&x2.0).reverse().then(x1.1.cmp(&x2.1)));

        return n_vs_word[..k as usize]
            .iter()
            .map(|x3| String::from(&x3.1))
            .collect();
    }
}

#[cfg(test)]
mod test {
    use crate::sorting::top_k_frequent_words::Solution;

    #[test]
    fn case01() {
        let words = vec!["i", "love", "leetcode", "i", "love", "coding"]
            .into_iter()
            .map(|x| x.to_string())
            .collect();
        let k = 2;
        let actual = Solution::top_k_frequent(words, k);
        let expected: Vec<String> = vec!["i", "love"]
            .into_iter()
            .map(|x| x.to_string())
            .collect();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let words = vec![
            "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is",
        ]
        .into_iter()
        .map(|x| x.to_string())
        .collect();
        let k = 4;
        let actual = Solution::top_k_frequent(words, k);
        let expected: Vec<String> = vec!["the", "is", "sunny", "day"]
            .into_iter()
            .map(|x| x.to_string())
            .collect();
        assert_eq!(actual, expected);
    }
}
