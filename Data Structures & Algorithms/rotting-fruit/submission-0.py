class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append([i,j])
        while q and fresh>0:
            for _ in range(len(q)):
                cy,cx = q.popleft()
                for dy, dx in dydx:
                    ny,nx = cy+dy, cx+dx
                    if 0<=ny<ROWS and 0<=nx<COLS and grid[ny][nx]==1:
                        grid[ny][nx] = 2
                        fresh-=1
                        q.append([ny,nx])
            time+=1
        return time if fresh==0 else -1
