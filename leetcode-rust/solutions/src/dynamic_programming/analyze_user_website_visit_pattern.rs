// https://leetcode-cn.com/problems/analyze-user-website-visit-pattern/
use std::collections::HashMap;

struct Solution;


impl Solution {
    pub fn most_visited_pattern(username: Vec<String>, timestamp: Vec<i32>, website: Vec<String>) -> Vec<String> {
        let mut username_vs_websites: HashMap<String, Vec<String>> = HashMap::new();
        let n = username.len();
        let mut most_pattern = String::new();
        let mut most_pattern_max_score = 0;

        for i in 0..n {
            match username_vs_websites.get_mut(&username[i]) {
                Some(w) => {
                    w.push(String::from(&website[i]))
                }
                None => {
                    username_vs_websites.insert(String::from(&username[i]), vec![String::from(&website[i])]);
                }
            }
        }

        let mut pattern_counter = HashMap::new();

        for (_, v) in username_vs_websites.into_iter() {
            if v.len() < 3 {
                continue;
            }
            for i in 0..v.len() - 2 {
                let key = v[i..i + 3].join("-");
                pattern_counter.insert(
                    String::from(&key), pattern_counter.get(&key).unwrap_or(&0) + 1,
                );
                if *(pattern_counter.get(&key).unwrap()) > most_pattern_max_score {
                    most_pattern_max_score = *pattern_counter.get(&key).unwrap();
                    most_pattern = key;
                } else if *(pattern_counter.get(&key).unwrap()) == most_pattern_max_score && most_pattern.ge(&key) {
                    most_pattern = key;
                }
            }
        }
        return most_pattern.split("-").map(str::to_string).collect();
    }
}

#[cfg(test)]
mod test {
    use std::slice::Iter;

    use crate::dynamic_programming::analyze_user_website_visit_pattern::Solution;

    fn to_vec_string(iter: Iter<&str>) -> Vec<String> {
        let mut vec_strings = vec![];
        for i in iter {
            vec_strings.push(i.to_string());
        }
        return vec_strings;
    }

    #[test]
    fn case01() {
        let username = to_vec_string(
            ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary", ].iter()
        );
        let timestamp = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        let website = to_vec_string(
            ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"].iter()
        );

        let actual = Solution::most_visited_pattern(username, timestamp, website);
        let expected = to_vec_string(["home", "about", "career"].iter());
        assert_eq!(actual, expected)
    }
}