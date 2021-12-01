class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result = []
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if result[-1][1]<intervals[i][0]:
                result.append(intervals[i])
            elif intervals[i][1]>result[-1][1]:
                result[-1][1] = intervals[i][1]
        return result
