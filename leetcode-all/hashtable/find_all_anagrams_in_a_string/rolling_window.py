class Solution:
    @staticmethod
    def a_z_counter(s):
        result = dict(zip(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z'], [0 for _ in range(26)]))
        for i in s:
            result[i] += 1
        return result

    def findAnagrams(self, s: str, p: str):
        result = []
        char_map_p = self.a_z_counter(p)
        char_map_window = self.a_z_counter(s[:len(p)])
        if char_map_p == char_map_window:
            result.append(0)

        for head in range(1, len(s) - len(p) + 1):
            tail = head + len(p)
            char_map_window[s[tail - 1]] += 1
            char_map_window[s[head - 1]] -= 1
            if char_map_window == char_map_p:
                result.append(head)

        return result


if __name__ == '__main__':
    t = '''cbaebabacd'''
    p = '''abc'''
    print(Solution().findAnagrams(t, p))
