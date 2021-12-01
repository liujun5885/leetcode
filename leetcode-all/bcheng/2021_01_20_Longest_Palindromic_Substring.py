from itertools import repeat, chain
class Solution:
    def expand(self, s, center):
        l, r = center-1, center+1
        while l>-1 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        #print(center, r-l-1)
        return r-l-1

    def longestPalindrome(self, s: str) -> str:
        filled_string = list(chain.from_iterable(zip(repeat(' '), s)))
        filled_string.append(' ')
        print(filled_string)
        center = max_len = 0
        for i in range(1,len(filled_string)-1):
            _len = self.expand(filled_string, i)
            if _len > max_len:
                center, max_len = i, _len
        left = center - max_len //2
        right = center + max_len //2
        return s[left//2 : (right-1)//2+1]
        
