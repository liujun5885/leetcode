// https://leetcode-cn.com/problems/triangle/submissions/
struct Solution;

impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let mut all_paths: Vec<Vec<i32>> = vec![];

        for i in 0..triangle.len() {
            let mut paths = vec![];
            for j in 0..triangle[i].len() {
                if i > 0 {
                    if j > 0 {
                        if all_paths[i - 1].len() > j {
                            paths.push(triangle[i][j] + all_paths[i - 1][j].min(all_paths[i - 1][j - 1]));
                        } else {
                            paths.push(triangle[i][j] + all_paths[i - 1][j - 1]);
                        }
                    } else {
                        paths.push(triangle[i][j] + all_paths[i - 1][j]);
                    }
                } else {
                    paths.push(triangle[i][j])
                }
            }
            all_paths.push(paths);
        }
        return *all_paths[all_paths.len() - 1].iter().min().unwrap();
    }
}

#[cfg(test)]
mod tests {
    use crate::dynamic_programming::triangle::Solution;

    #[test]
    fn case01() {
        let triangle = vec![vec![2], vec![3, 4], vec![6, 5, 7], vec![4, 1, 8, 3]];
        let expected = 11;
        let actual = Solution::minimum_total(triangle);
        assert_eq!(actual, expected);
    }

    #[test]
    fn case02() {
        let triangle = vec![vec![2]];
        let expected = 2;
        let actual = Solution::minimum_total(triangle);
        assert_eq!(actual, expected);
    }
}
