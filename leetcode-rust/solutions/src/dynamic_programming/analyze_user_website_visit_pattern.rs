// https://leetcode-cn.com/problems/analyze-user-website-visit-pattern/
use std::collections::{HashMap, HashSet};

struct Solution;


impl Solution {
    pub fn most_visited_pattern(username: Vec<String>, timestamp: Vec<i32>, website: Vec<String>) -> Vec<String> {
        let mut username_vs_websites: HashMap<String, Vec<String>> = HashMap::new();
        let n = username.len();
        let mut most_pattern = String::new();
        let mut most_pattern_max_score = 0;

        let mut timestamp_username_website = vec![];
        for i in 0..n {
            timestamp_username_website.push(
                (timestamp[i], String::from(&username[i]), String::from(&website[i]))
            );
        }
        timestamp_username_website.sort_by(|x1, x2| x1.0.cmp(&x2.0));

        for i in 0..n {
            match username_vs_websites.get_mut(&timestamp_username_website[i].1) {
                Some(w) => {
                    w.push(String::from(&timestamp_username_website[i].2))
                }
                None => {
                    username_vs_websites.insert(
                        String::from(&timestamp_username_website[i].1),
                        vec![String::from(&timestamp_username_website[i].2)],
                    );
                }
            }
        }

        let mut pattern_counter = HashMap::new();

        for (_, v) in username_vs_websites.into_iter() {
            if v.len() < 3 {
                continue;
            }

            let mut paths = HashSet::new();

            for i in 0..v.len() {
                for j in i + 1..v.len() {
                    for k in j + 1..v.len() {
                        let key = format!("{}-{}-{}", v[i], v[j], v[k]);
                        paths.insert(String::from(&key));
                    }
                }
            }

            for path in paths.iter() {
                pattern_counter.insert(
                    String::from(path), pattern_counter.get(path).unwrap_or(&0) + 1,
                );
                if *(pattern_counter.get(path).unwrap()) > most_pattern_max_score {
                    most_pattern_max_score = *pattern_counter.get(path).unwrap();
                    most_pattern = String::from(path);
                } else if *(pattern_counter.get(path).unwrap()) == most_pattern_max_score && most_pattern.ge(path) {
                    most_pattern = String::from(path);
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

    #[test]
    fn case02() {
        let username = to_vec_string(
            ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"].iter()
        );
        let timestamp = vec![436363475, 710406388, 386655081, 797150921];
        let website = to_vec_string(
            ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"].iter()
        );

        let actual = Solution::most_visited_pattern(username, timestamp, website);
        let expected = to_vec_string(["oz", "mryxsjc", "wlarkzzqht"].iter());
        assert_eq!(actual, expected)
    }

    #[test]
    fn case03() {
        let username = to_vec_string(
            ["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"].iter()
        );
        let timestamp = vec![527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079, 317455832, 411747930];
        let website = to_vec_string(
            ["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "yljmntrclw", "hibympufi", "yljmntrclw"].iter()
        );

        let actual = Solution::most_visited_pattern(username, timestamp, website);
        let expected = to_vec_string(["hibympufi", "hibympufi", "yljmntrclw"].iter());
        assert_eq!(actual, expected)
    }
}