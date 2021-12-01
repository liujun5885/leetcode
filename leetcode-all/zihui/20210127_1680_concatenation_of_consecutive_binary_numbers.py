class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ''
        MOD = 10 ** 9 + 7
        for i in range(n + 1):
            s += bin(i)[2:]
        return int(s, 2) % MOD
