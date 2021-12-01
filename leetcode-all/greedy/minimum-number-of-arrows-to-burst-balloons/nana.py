from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return len(intervals)
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            elif intervals[i][1] < result[-1][1]:
                result[-1][1] = min(intervals[i][1], result[-1][1])
        print(result)
        return(len(result))


if __name__ == '__main__':
    v = [[10,16],[2,8],[1,6],[7,12]]
    print(Solution().merge(v))
    v = [[1,2],[3,4],[5,6],[7,8]]
    print(Solution().merge(v))
    v= [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
    print(Solution().merge(v))

