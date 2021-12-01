# run
# pytest replace_words/asher.py

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        shortest_root = None
        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root) and (not shortest_root or len(shortest_root) > len(root)):
                    shortest_root = root

            if shortest_root:
                words[i] = shortest_root
            shortest_root = None

        return ' '.join(words)


#
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         words = sentence.split()
#         shortest_root = None
#         tmp_store = {}
#         for i in range(len(words)):
#             if words[i] in tmp_store:
#                 if tmp_store[words[i]]:
#                     words[i] = tmp_store[words[i]]
#                 continue
#             for root in dictionary:
#                 if words[i].startswith(root) and (not shortest_root or len(shortest_root) > len(root)):
#                     shortest_root = root
#             if shortest_root:
#                 tmp_store[words[i]] = shortest_root
#                 words[i] = shortest_root
#             else:
#                 tmp_store[words[i]] = None
#
#             shortest_root = None
#
#         return ' '.join(words)

def test_case1():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    expected = "the cat was rat by the bat"
    actual = Solution().replaceWords(dictionary, sentence)
    assert actual == expected


def test_case2():
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    expected = "a a b c"
    actual = Solution().replaceWords(dictionary, sentence)
    assert actual == expected


def test_case3():
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    expected = "a a a a a a a a bbb baba a"
    actual = Solution().replaceWords(dictionary, sentence)
    assert actual == expected


def test_case4():
    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    expected = "the cat was rat by the bat"
    actual = Solution().replaceWords(dictionary, sentence)
    assert actual == expected


def test_case5():
    dictionary = ["ac", "ab"]
    sentence = "it is abnormal that this solution is accepted"
    expected = "it is ab that this solution is ac"
    actual = Solution().replaceWords(dictionary, sentence)
    assert actual == expected
