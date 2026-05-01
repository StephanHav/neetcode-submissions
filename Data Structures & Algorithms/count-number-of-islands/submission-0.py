class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def setToZero(y, x):
            grid[y][x] = "0"
            
            coords = [[y+1, x],
                        [y-1, x],
                        [y, x+1],
                        [y, x-1]]
        
            for coord in coords:
                if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and grid[coord[0]][coord[1]] == "1":
                    setToZero(coord[0], coord[1])
            return
                
        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    setToZero(y, x)
                    islands += 1
        return islands
