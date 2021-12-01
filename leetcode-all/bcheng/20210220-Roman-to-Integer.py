class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = list(reversed(s))
        last = _sum = symbol_mapping[s[0]]
        for i in s[1:]:
            cur = symbol_mapping[i]
            if cur>= last:
                _sum += cur
            else:
                _sum -= cur
            last = cur
        return _sum
