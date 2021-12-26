// https://leetcode-cn.com/problems/most-common-word/submissions/
use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    pub fn most_common_word(paragraph: String, banned: Vec<String>) -> String {
        let mut banned_set = HashSet::new();
        let mut str_map = HashMap::new();
        let mut max_num = 0;
        let mut ans = "".to_string();

        for i in banned.iter() {
            banned_set.insert(i.to_lowercase());
        }

        for i in paragraph.replace(&[',', '\"', '.', ';', ':', '\'', '!', '?'][..], " ").split(' ').into_iter() {
            let p = i.to_lowercase();
            if p.len() == 0 || banned_set.contains(&p) {
                continue;
            }
            if str_map.contains_key(&p) {
                str_map.insert(p.clone(), str_map[&p] + 1);
            } else {
                str_map.insert(p.clone(), 1);
            }
            if str_map[&p] > max_num {
                max_num = str_map[&p];
                ans = p.clone();
            }
        }

        return ans;
    }
}

#[cfg(test)]
mod test {
    use crate::hash_table::most_common_word::Solution;

    #[test]
    fn case01() {
        let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.".to_string();
        let banned = vec!["hit".to_string()];

        let actual = Solution::most_common_word(paragraph, banned);
        let expected = "ball".to_string();
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let paragraph = "a, a, a, a, b,b,b,c, c".to_string();
        let banned = vec!["a".to_string()];

        let actual = Solution::most_common_word(paragraph, banned);
        let expected = "b".to_string();
        assert_eq!(actual, expected);
    }
}