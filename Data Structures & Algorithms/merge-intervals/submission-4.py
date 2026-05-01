class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        start_prev = intervals[0][0]
        end_prev = intervals[0][1]
        res = [intervals[0]]
        ptr = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end_prev:
                new_end = max(intervals[i][1], end_prev)
                new_start = min(intervals[i][0], start_prev)
                
                res[ptr] = [new_start, new_end]
                start_prev, end_prev = new_start, new_end
            else:
                ptr += 1
                res.append(intervals[i])
                start_prev, end_prev = intervals[i][0], intervals[i][1]
        return res
                
    # intervals=[[1,3],[2,3],[2,2],[2,2],[3,3],i[4,6],[5,7]]
    # start_prev = 4
    # end_prev = 6
    # res = [[1,3],[4,6]]
    # ptr = 1
    # i = 5
    # new_end = 3
    # new_start = 1

