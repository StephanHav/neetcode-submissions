class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        removed = 0

        for i, iv in enumerate(intervals[1:]):
            if iv[0] < prev_end:
                removed += 1
                prev_end = min(prev_end, iv[1])
            else:
                prev_end = iv[1]
        return removed

    # intervals=[[-73,-26],[-65,-11],[-63,2],[-62,-49],[-52,31],[-40,-26],[-31,49],[30,47],[58,95],[66,98],[82,97],[95,99]]
    # prev_start = 58
    # prev_end = 95
    # removed = 6
    # i = 7