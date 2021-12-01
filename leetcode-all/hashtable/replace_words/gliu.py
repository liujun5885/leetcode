from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        if sentence == "":
            return sentence
        tree = {}
        self.build_word_tree(tree, dictionary)
        result = ""
        for word in sentence.split(" "):
            result += (self.extract_word(tree, word) + " ")
        return result[:-1]

    def extract_word(self, tree, word) -> str:
        cur_pos = tree
        for ch in word:
            if not cur_pos.get(ch):
                return word
            else:
                if cur_pos[ch].get('$'):
                    return cur_pos[ch]['$']
                cur_pos = cur_pos[ch]
        return word

    def build_word_tree(self, tree, dictionary: List[str]):
        for word in dictionary:
            cur_pos = tree
            for ch in word:
                if not cur_pos.get(ch):
                    cur_pos[ch] = {}
                elif cur_pos.get('$'):
                    cur_pos = None
                    break
                cur_pos = cur_pos[ch]
            if cur_pos is not None:
                cur_pos['$'] = word

    def main(self):
        print(self.replaceWords(dictionary=["cat","bat","rat"], sentence="the cattle was rattled by the battery"))

if __name__ == '__main__':
    Solution().main()
