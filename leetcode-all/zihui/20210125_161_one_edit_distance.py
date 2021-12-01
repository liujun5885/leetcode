"""
给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。

注意：

满足编辑距离等于 1 有三种可能的情形：

往 s 中插入一个字符得到 t
从 s 中删除一个字符得到 t
在 s 中替换一个字符得到 t

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if abs(len_s - len_t) > 1:
            return False
        
        if len_s < len_t:
            return self.isOneEditDistance(t, s)

        for i in range(len_t):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
        
        return len_s != len_t


if __name__ == '__main__':
    cases = [
        ({'s': 'ab', 't': 'acb'}, True),
        ({'s': 'cab', 't': 'ad'}, False),
        ({'s': '1203', 't': '1213'}, True),
        ({'s': 'b', 't': ''}, True),
        ({'s': 'ab', 't': 'ab'}, False),
        ({'s': 'ab', 't': 'ba'}, False),
        ({'s': 'a', 't': 'A'}, True),
        ({'s': '', 't': ''}, False),
    ]
    for case in cases:
        input, output = case
        assert Solution().isOneEditDistance(**input) == output
