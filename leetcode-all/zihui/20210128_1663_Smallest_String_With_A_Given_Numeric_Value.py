class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        BASE = ord('a') - 1
        ans = ''
        
        while n > 0:
            a = k // 26
            b = k % 26
            r = True if b else False
            
            if n == a + r:
                ans += chr(b + BASE) if r else ''
                ans += 'z' * a
                return ans
            else:
                m = n - (a + r)
                ans += 'a' * m
                k -= m
                n -= m
        ans += chr(b + BASE) if r else ''
        ans += 'z' * a
        return ans
