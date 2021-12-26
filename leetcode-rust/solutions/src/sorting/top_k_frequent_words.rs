// https://leetcode-cn.com/problems/top-k-frequent-words/
use counter::Counter;

struct Solution {}


impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        let word_counter = words.into_iter().collect::<Counter<_>>();
        let sorted_words = word_counter.most_common_tiebreaker(
            |x1, x2| { x2.cmp(&x1) }
        );
        let ans = sorted_words[..k as usize].iter().map(|x| { String::from(&x.0) }).collect::<Vec<_>>();
        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::sorting::top_k_frequent_words::Solution;

    #[test]
    fn case01() {
        let words = vec![
            "i", "love", "leetcode", "i", "love", "coding",
        ].into_iter().map(|x| { x.to_string() }).collect();
        let k = 2;
        let mut actual = Solution::top_k_frequent(words, k);
        let mut expected: Vec<String> = vec!["i", "love"].into_iter().map(|x| { x.to_string() }).collect();
        assert_eq!(actual.sort_unstable(), expected.sort_unstable());
    }
}