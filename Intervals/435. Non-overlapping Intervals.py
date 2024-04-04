class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        counter = 0
        last_interval = intervals[0]
        for i in intervals:
            start = i[0]
            end = i[1]
            last_end = last_interval[1]
            if start>=last_end:
                last_interval=i
            elif end>=last_end:
                counter+=1
            elif end<last_end:
                last_interval=i
                counter+=1
        return counter-1