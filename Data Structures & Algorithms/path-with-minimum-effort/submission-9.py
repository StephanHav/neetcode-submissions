class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        visited = set()
        minheap = []
        heapq.heappush(minheap, (0,(0,0)))
        cols = len(heights[0])-1
        rows = len(heights)-1

        while minheap:
            curr = heapq.heappop(minheap)

            if curr[1] in visited:
                continue
            visited.add(curr[1])

            if curr[1] == (rows,cols):
                return curr[0]

            for move in moves:
                new = (curr[1][0]+move[0], curr[1][1]+move[1])
                if 0 <= new[1] <= cols and 0 <= new[0] <= rows:
                    diff = abs(heights[new[0]][new[1]] - heights[curr[1][0]][curr[1][1]]) 
                    entry = (max(curr[0], diff), new)
                    heapq.heappush(minheap, entry)



