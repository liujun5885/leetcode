class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        # if p's second char is not '*', compare current first characters to see if they are the same
        # if p's second char is '*', which means we can either 1. ignore the char before '*' - same as matching zero times
        # or 2. try to match '*' more than one times
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (len(s) > 0 and self.has_same_first_letters(s, p) and self.isMatch(s[1:], p))
        else:
            return len(s) > 0 and self.has_same_first_letters(s, p) and self.isMatch(s[1:], p[1:])

    def has_same_first_letters(self, s: str, p: str) -> bool:
        return s[0] == p[0] or p[0] == '.'
