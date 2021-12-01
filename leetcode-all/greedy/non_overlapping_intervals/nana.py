class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 1:
            return len(intervals)
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1] <= intervals[i][0]:
                result.append(intervals[i])
            elif intervals[i][1] < result[-1][1]:
                result.pop()
                result.append(intervals[i])
        count = len(intervals) - len(result)
        return count
if __name__ == '__main__':
    v = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(Solution().merge(v))

