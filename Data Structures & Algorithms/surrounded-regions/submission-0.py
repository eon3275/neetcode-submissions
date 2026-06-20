class Solution: #dfs
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dydx = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            board[r][c]='#'
            for dy, dx in dydx:
                ny, nx = dy+r, dx+c
                if 0<=ny<ROWS and 0<=nx<COLS and board[ny][nx]=='O':
                    dfs(ny,nx)
        for r in range(ROWS):
            if board[r][0]=='O':
                dfs(r,0)
            if board[r][COLS-1]=='O':
                dfs(r,COLS-1)
        for c in range(COLS):
            if board[0][c]=='O':
                dfs(0,c)
            if board[ROWS-1][c]=='O':
                dfs(ROWS-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='#':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'