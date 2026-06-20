class Solution: #dfs
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        p_reach = set()
        a_reach = set()
        def dfs(r, c, reach):
            reach.add((r,c))
            for dy, dx in dydx:
                ny, nx = r+dy, c+dx
                if 0<=ny<ROWS and 0<=nx<COLS and (ny,nx) not in reach and heights[ny][nx]>=heights[r][c]:
                    dfs(ny, nx, reach)
        for r in range(ROWS):
            dfs(r, 0, p_reach)
            dfs(r, COLS-1, a_reach)
        for c in range(COLS):
            dfs(0, c, p_reach)
            dfs(ROWS-1, c, a_reach)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in p_reach and (r,c) in a_reach:
                    res.append([r,c])
        return res