class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or r==ROWS-1 or c==0 or c==COLS-1:
                    if board[r][c]=='O':
                        q.append((r,c))
                        board[r][c] = '#'
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