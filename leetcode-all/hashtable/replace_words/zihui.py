from collections import Counter
from typing import List, Set


class Solution:
    @staticmethod
    def replace(word: str, roots: Set[str]):
        for i in range(1, len(word)):
            if word[:i] in roots:
                return word[:i]
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        new_sentence = " ".join([self.replace(word, roots) for word in sentence.split()])
        return new_sentence


if __name__ == '__main__':
    assert Solution().replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa") == "a a a a a a a a bbb baba a"

    assert Solution().replaceWords(
        dictionary=["a","b","c"],
        sentence="aadsfasf absbs bbab cadsfafs") == "a a b c"
