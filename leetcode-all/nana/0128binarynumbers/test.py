class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        s = ''.join("{0:b}".format(i) for i in range(1,n+1))
        return int(s,2)%mod