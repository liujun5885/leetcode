from typing import List


class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = []

        rain_dict = {}
        drain_list = []

        for i in range(len(rains)):
            if rains[i] == 0:
                drain_list.append(i)
                ans.append(1)
            elif rains[i] > 0:
                if rains[i] not in rain_dict:
                    rain_dict[rains[i]] = i
                    ans.append(-1)
                else:
                    find = 0
                    for d in drain_list:
                        if d > rain_dict[rains[i]]:
                            find = d
                            break
                    if find == 0:
                        return []
                    else:
                        drain_list.remove(find)
                        rain_dict[rains[i]] = i
                        ans[find] = rains[i]
                        ans.append(-1)

        return ans


def test_case1():
    rains = [1, 2, 3, 4]
    actual = Solution().avoidFlood(rains)
    expected = [-1, -1, -1, -1]
    assert actual == expected


def test_case2():
    rains = [1, 2, 0, 0, 2, 1]
    expected = [-1, -1, 2, 1, -1, -1]
    actual = Solution().avoidFlood(rains)
    assert actual == expected


def test_case3():
    rains = [1, 2, 0, 1, 2]
    expected = []
    actual = Solution().avoidFlood(rains)
    assert actual == expected


def test_case4():
    rains = [69, 0, 0, 0, 69]
    expected = [-1, 69, 1, 1, -1]
    actual = Solution().avoidFlood(rains)
    assert actual == expected


def test_case5():
    rains = [10, 20, 20]
    expected = []
    actual = Solution().avoidFlood(rains)
    assert actual == expected


def test_case6():
    rains = [1, 2, 0, 2, 3, 0, 1]
    expected = [-1, -1, 2, -1, -1, 1, -1]
    actual = Solution().avoidFlood(rains)
    assert actual == expected


def test_case7():
    rains = [0, 1, 1]
    expected = []
    actual = Solution().avoidFlood(rains)
    assert actual == expected


if __name__ == '__main__':
    Solution().avoidFlood([1, 2, 3])
