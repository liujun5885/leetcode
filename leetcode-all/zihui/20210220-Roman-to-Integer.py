iclass Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        reduce_mapping = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
        ans = 0
        prev = None
        for i in s[::-1]:
            if prev and i == reduce_mapping.get(prev):
                ans -= roman_int_mapping.get(i)
            elif prev:
                ans += roman_int_mapping.get(i)
            else:
                ans += roman_int_mapping.get(i)
            prev = i
        return ans

