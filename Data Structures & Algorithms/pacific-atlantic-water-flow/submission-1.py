class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        rows, cols = len(heights), len(heights[0])
        pac_queue = deque()
        atl_queue = deque()

        for i in range(rows):
            pac_queue.append((i, 0))
            atl_queue.append((i, cols-1))
        
        for i in range(cols):
            pac_queue.append((0, i))
            atl_queue.append((rows-1, i))

        pac_visited = set(pac_queue)
        atl_visited = set(atl_queue)
        
        res = []

        def bfs(queue, visited):
            while queue:

                r, c = queue.popleft()
                directions = [(-1, 0),
                            (1, 0),
                            (0, -1),
                            (0, 1)
                ]
                
                for rc, cc in directions:
                    rn, cn = r + rc, c + cc
                    if 0 <= rn < rows and 0 <= cn < cols: 
                        if (rn, cn) not in visited and heights[rn][cn] >= heights[r][c]:
                            queue.append((rn,cn))
                            visited.add((rn, cn))
        
        bfs(pac_queue, pac_visited)
        bfs(atl_queue, atl_visited)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_visited and (r, c) in atl_visited:
                    res.append((r,c))
        return res
            
            