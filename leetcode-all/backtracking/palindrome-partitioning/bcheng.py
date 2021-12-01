class Solution:
    @staticmethod
    def is_palindromic(s):
        lens = len(s)
        return s[:lens // 2] == s[(lens + 1) // 2:][::-1]

    def split(self, index):
        if index == self.lens:
            self.res.append(self.path[:])
            return
        for i in range(index + 1, self.lens+1):
            if self.is_palindromic(self.s[index:i]):
                self.path.append(self.s[index:i])
                self.split(i)
                self.path.pop()

    def partition(self, s: str):
        self.res = []
        self.path = []
        self.s = s
        self.lens = len(s)
        self.split(0)
        return self.res
