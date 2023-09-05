// https://leetcode.cn/problems/happy-number/

struct Solution;
impl Solution {
    pub fn square_sum(n: i32) -> i32 {
        let mut n = n;
        let mut sum = 0;
        while n > 0 {
            let digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        sum
    }

    pub fn is_happy(n: i32) -> bool {
        let mut slow = n;
        let mut fast = Solution::square_sum(n);
        while slow != fast {
            slow = Solution::square_sum(slow);
            fast = Solution::square_sum(Solution::square_sum(fast));
            if slow == 1 || fast == 1 {
                return true;
            }
        }
        slow == 1 || fast == 1
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let n = 19;
        let expected = true;
        assert_eq!(expected, Solution::is_happy(n));
    }

    #[test]
    fn case02() {
        let n = 2;
        let expected = false;
        assert_eq!(expected, Solution::is_happy(n));
    }
}
