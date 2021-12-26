use std::collections::HashMap;

struct Solution;


impl Solution {
    pub fn most_visited_pattern(username: Vec<String>, timestamp: Vec<i32>, website: Vec<String>) -> Vec<String> {
        let mut username_vs_websites = HashMap::new();
        let n = username.len();

        for i in 0..n {
            if username_vs_websites.contains_key(&username[i]) {
                username_vs_websites.get(&username[i]).unwrap().append(website[i].clone());
            } else {
                username_vs_websites.insert(username[i].clone(), vec![website[i].clone()]);
            }
        }

        return vec!["home".to_string(), "about".to_string(), "career".to_string()];
    }
}

#[cfg(test)]
mod test {
    use std::slice::Iter;

    use crate::analyze_user_website_visit_pattern::Solution;

    fn to_vec_string(iter: Iter<&str>) -> Vec<String> {
        let mut vec_strings = vec![];
        for i in iter {
            vec_strings.push(i.to_string());
        }
        return vec_strings;
    }

    #[test]
    fn case01() {
        let mut username = to_vec_string(
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