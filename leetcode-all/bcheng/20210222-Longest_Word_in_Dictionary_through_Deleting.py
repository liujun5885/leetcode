class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s:
            return ''
        d.sort(key = lambda x: (-len(x), x))
        s_len = len(s)
        for word in d:
            i=0
            for char in word:
                while i<s_len and s[i]!=char:
                    i+=1
                if i>=s_len:
                    break
                i+=1
            else:
                return word
        return ''

