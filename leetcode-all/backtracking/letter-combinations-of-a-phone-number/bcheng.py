class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        temp = []

        def convert(index):
            if index == len(digits):
                res.append(''.join(temp))
                return
            for char in mapping[digits[index]]:
                temp.append(char)
                convert(index + 1)
                temp.pop()

        convert(0)
        return res
