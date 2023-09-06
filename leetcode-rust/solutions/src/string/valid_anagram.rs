// https://leetcode.cn/problems/valid-anagram/

struct Solution;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_map = vec![0; 26];
        let mut t_map = vec![0; 26];

        for c in s.chars() {
            s_map[c as usize - 'a' as usize] += 1;
        }
        for c in t.chars() {
            t_map[c as usize - 'a' as usize] += 1;
        }

        s_map == t_map
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let s = "anagram".to_string();
        let t = "nagaram".to_string();
        let expected = true;
        assert_eq!(expected, Solution::is_anagram(s, t));
    }

    #[test]
    fn case02() {
        let s = "rat".to_string();
        let t = "car".to_string();
        let expected = false;
        assert_eq!(expected, Solution::is_anagram(s, t));
    }
}
