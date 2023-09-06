// https://leetcode.cn/problems/isomorphic-strings/

struct Solution;
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let mut map_s = std::collections::HashMap::new();
        let mut map_t = std::collections::HashMap::new();

        if s.len() != t.len() {
            return false;
        }

        let mut s_chars = s.chars();
        let mut t_chars = t.chars();
        for i in 0..s.len() {
            let s_c = s_chars.next().unwrap();
            let t_c = t_chars.next().unwrap();

            if map_s.insert(s_c, i) != map_t.insert(t_c, i) {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let s = "egg".to_string();
        let t = "add".to_string();
        let expected = true;
        assert_eq!(expected, Solution::is_isomorphic(s, t));
    }

    #[test]
    fn case02() {
        let s = "foo".to_string();
        let t = "bar".to_string();
        let expected = false;
        assert_eq!(expected, Solution::is_isomorphic(s, t));
    }

    #[test]
    fn case03() {
        let s = "paper".to_string();
        let t = "title".to_string();
        let expected = true;
        assert_eq!(expected, Solution::is_isomorphic(s, t));
    }
}
