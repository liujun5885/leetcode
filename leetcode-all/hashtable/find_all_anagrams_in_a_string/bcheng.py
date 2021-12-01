from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        lp = len(p)
        right = len(p) - 1
        left = 0
        counter = Counter(p)
        window = Counter(s[:len(p)])
        while right < len(s):
            if counter == window:
                res.append(left)
            right += 1
            left += 1
            window[s[right]] += 1
            window[s[left]] -= 1
            if window[s[left]] == 0:
                window.pop(s[left])
        return res
