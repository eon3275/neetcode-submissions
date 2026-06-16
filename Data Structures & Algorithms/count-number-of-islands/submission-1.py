class Solution: #bfs
    def numIslands(self, grid: List[List[str]]) -> int:
      res = 0
      ROWS, COLS = len(grid), len(grid[0])
      dydx = [[1,0],[-1,0],[0,1],[0,-1]]
      for r in range(ROWS):
        for c in range(COLS):
          if grid[r][c]=='1':
            res+=1
            q = deque()
            q.append([r,c])
            grid[r][c] = '#'
            while q:
              cy, cx = q.popleft()
              for dy, dx in dydx:
                ny, nx = cy+dy, cx+dx
                if 0<=ny<ROWS and 0<=nx<COLS and grid[ny][nx] == '1':
                  grid[ny][nx] = '#'
                  q.append([ny,nx])
      return res