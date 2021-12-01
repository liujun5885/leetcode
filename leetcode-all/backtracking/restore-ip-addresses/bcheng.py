class Solution:
    def build(self, start, dots):
        if dots == 0:
            part = self.s[start:]
            if int(part) < 256:
                if part[0]!='0' or len(part) == 1:
                    self.path.append(part)
                    self.res.append('.'.join(self.path))
                    self.path.pop()
        else:
            for i in range(1, 4):
                if start+i >= self.len:
                    break
                part = self.s[start:start+i]
                if part[0] == '0' and i > 1:
                    break
                if int(part) < 256 and self.len-(start+i)<=3*dots:
                    self.path.append(part)
                    self.build(start+i, dots-1)
                    self.path.pop()

    def restoreIpAddresses(self, s: str):
        self.len = len(s)
        self.path = []
        self.s = s
        self.res = []
        self.build(0, 3)
        return self.res
