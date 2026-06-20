class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        for r in range(ROWS):
            if board[r][0]=='O':
                board[r][0] = '#'
                q.append((r,0))
            if board[r][COLS-1]=='O':
                board[r][COLS-1] = '#'
                q.append((r,COLS-1))
        for c in range(COLS):
            if board[0][c]=='O':
                board[0][c] = '#'
                q.append((0,c))
            if board[ROWS-1][c]=='O':
                board[ROWS-1][c] = '#'
                q.append((ROWS-1,c))
        while q:
            cy,cx = q.popleft()
            for dy, dx in dydx:
                ny,nx = cy+dy,cx+dx
                if 0<=ny<ROWS and 0<=nx<COLS and board[ny][nx]=='O':
                     board[ny][nx] = '#'
                     q.append((ny,nx))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'