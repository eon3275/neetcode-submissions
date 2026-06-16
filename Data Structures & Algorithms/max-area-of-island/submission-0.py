class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    q = deque([[r, c]])
                    grid[r][c] = 0
                    area = 1
                    while q:
                        cy,cx = q.popleft()
                        for dy,dx in dydx:
                            ny,nx=cy+dy,cx+dx
                            if 0<=ny<ROWS and 0<=nx<COLS and grid[ny][nx]:
                                q.append([ny,nx])
                                grid[ny][nx] = 0
                                area+=1
                    res = max(res, area)
        return res