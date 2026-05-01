class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        coords = [(1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)]

        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    islands += 1

                    stack = [(y, x)]
                    grid[y][x] = "0"
                    while stack:
                        curr_y, curr_x = stack.pop()
                        for yc, xc in coords:
                            if 0 <= (curr_y + yc) < len(grid) and 0 <= (curr_x + xc) < len(grid[0]) and grid[curr_y + yc][curr_x + xc] == "1":
                                grid[curr_y + yc][curr_x + xc] = "0"
                                stack.append((curr_y + yc, curr_x + xc))


        return islands


        # def setToZero(y, x):
        #     grid[y][x] = "0"
            
        #     coords = [[y+1, x],
        #                 [y-1, x],
        #                 [y, x+1],
        #                 [y, x-1]]
        
        #     for coord in coords:
        #         if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and grid[coord[0]][coord[1]] == "1":
        #             setToZero(coord[0], coord[1])
        #     return