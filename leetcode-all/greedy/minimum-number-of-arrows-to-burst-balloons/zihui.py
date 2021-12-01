class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)

        points = sorted(points)
        overlaps = [points[0]]
        for point in points[1:]:
            overlap = overlaps[-1]
            if point[0] <= overlap[1]:
                overlaps[-1] = [max(point[0], overlap[0]), min(point[1], overlap[1])]
            else:
                overlaps.append(point)
        return len(overlaps)
