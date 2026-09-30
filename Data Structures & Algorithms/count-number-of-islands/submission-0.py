class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [0,1], [-1, 0], [0, -1]] 
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(x, y):
            q = deque()
            grid[x][y] = "0"
            q.append((x,y))

            while q:
                row, col = q.popleft()
                for dx, dy in directions:
                    newX, newY = dx + row, dy + col
                    
                    if(newX < 0 or newY < 0 or newX >= rows or newY >= cols or grid[newX][newY] == "0"):
                        continue
                    q.append((newX, newY))
                    grid[newX][newY] = "0"
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1

        

        return islands