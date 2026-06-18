class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2**31-1
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c]:
                    q.append([r,c])
        while q:
            cy,cx=q.popleft()
            for dy, dx in dydx:
                ny,nx=cy+dy,cx+dx
                if 0<=ny<ROWS and 0<=nx<COLS and grid[ny][nx] == INF:
                    grid[ny][nx] = grid[cy][cx]+1
                    q.append([ny,nx])
        