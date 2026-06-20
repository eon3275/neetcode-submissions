class Solution: #bfs
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        ROWS, COLS = len(heights), len(heights[0])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        res = []
        a_q = deque()
        a_s = set()
        p_q = deque()
        p_s = set()
        for r in range(ROWS):
            p_q.append((r, 0))
            p_s.add((r, 0))
            a_q.append((r, COLS-1))
            a_s.add((r, COLS-1))
        for c in range(COLS):
            p_q.append((0, c))
            p_s.add((0,c))
            a_q.append((ROWS-1,c))
            a_s.add((ROWS-1,c))
        def bfs(q, s):
            while q:
                cy, cx = q.popleft()
                for dy,dx in dydx:
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<ROWS and 0<=nx<COLS and (ny, nx) not in s and heights[ny][nx]>=heights[cy][cx]:
                        q.append((ny,nx))
                        s.add((ny,nx))
        bfs(p_q,p_s)
        bfs(a_q,a_s)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in p_s and (r,c) in a_s:
                    res.append([r,c])
        return res