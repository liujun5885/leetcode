from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = ''
        # for i in range(len(s)):
        #     start = max(0, i - len(res) - 1)
        #     temp = s[start: i + 1]
        #     if temp == temp[:: -1]:
        #         res = temp
        #     else:
        #         temp = temp[1:]
        #         if temp == temp[::-1]:
        #             res = temp
        # return res

        maxPal = ''
        for i in range(len(s)):
            maxPal = max(maxPal, self.largestPalindrome(s, i - 1, i), self.largestPalindrome(s, i - 1, i + 1),
                         key=len)
        return maxPal

    def largestPalindrome(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return s[i + 1:j]

s='abba'
res = Solution().longestPalindrome(s)
print(res)
