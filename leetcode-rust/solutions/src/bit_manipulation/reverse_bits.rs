// https://leetcode.cn/problems/reverse-bits/

struct Solution;

impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut x = x;
        let mut result = 0;
        for _ in 0..32 {
            result <<= 1;
            result |= x & 1;
            x >>= 1;
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case01() {
        let x = 0b00000010100101000001111010011100;
        let expected = 0b00111001011110000010100101000000;
        assert_eq!(expected, Solution::reverse_bits(x));
    }

    #[test]
    fn case02() {
        let x = 0b11111111111111111111111111111101;
        let expected = 0b10111111111111111111111111111111;
        assert_eq!(expected, Solution::reverse_bits(x));
    }
}
