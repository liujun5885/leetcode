class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        return c1 == c2 or (set(list(c1.keys())) == set(list(c2.keys())) and sorted(c1.values()) == sorted(c2.values()))
