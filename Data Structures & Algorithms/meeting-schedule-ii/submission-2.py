"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s = 0
        e = 0
        res = 0
        occupied = 0
        while s < len(starts):

            if starts[s] < ends[e]:
                s += 1
                occupied += 1
            else:
                e += 1
                occupied -= 1
            res = max(res, occupied)
        return res