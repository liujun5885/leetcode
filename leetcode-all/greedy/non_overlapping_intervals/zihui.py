class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals)
        new = [intervals[0]]
        for row in intervals[1:]:
            x1, y1 = new[-1]
            x2, y2 = row

            if x2 < y1:
                if y2 < y1:
                    new[-1] = [x2, y2]
            else:
                new.append([x2, y2])
        return len(intervals) - len(new)
