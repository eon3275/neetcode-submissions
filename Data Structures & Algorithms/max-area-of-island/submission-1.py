class Solution: #dfs
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dydx=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            if not(0<=r<ROWS and 0<=c<COLS) or not grid[r][c]:
                return 0
            area = 1
            grid[r][c]=0
            for dy,dx in dydx:
                area+=dfs(r+dy, c+dx)
            return area
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res=max(res, dfs(r,c))
        return res