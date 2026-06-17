class Solution: #dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dydx=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            area = 1
            for dy,dx in dydx:
                ny,nx = r+dy, c+dx
                if 0<=ny<ROWS and 0<=nx<COLS and grid[ny][nx]:
                    grid[ny][nx] = 0
                    area+=dfs(ny, nx)
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    grid[r][c] = 0
                    res=max(res, dfs(r,c))
        return res