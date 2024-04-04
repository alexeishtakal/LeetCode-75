class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        last_interval = points[0]
        counter = 0
        for i in points:
            start = i[0]
            end = i[1]
            last_end = last_interval[1]
            if start > last_end:
                last_interval = i
            elif end > last_end:
                counter += 1
            elif end <= last_end:
                last_interval = i
                counter += 1
        return len(points) - (counter - 1)
