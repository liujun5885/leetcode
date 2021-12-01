class Solution:
    def expend_from_middle(self, s, l, r):
        if not s or l > r: 
            return 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
        
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        start, end = 0, 0
        for i in range(len(s)):
            len_odd = self.expend_from_middle(s, i, i)
            len_even = self.expend_from_middle(s, i, i + 1)
            curr_len = max(len_odd, len_even)
            
            if curr_len > end - start:
                start = i - (curr_len - 1)// 2
                end = i + curr_len // 2

        return s[start: end + 1]  
