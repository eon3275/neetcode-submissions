class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diagPos = set()
        diagNeg = set()
        board = [['.']*n for _ in range(n)]
        def backtracking(r):
            if r==n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r+c in diagPos or r-c in diagNeg:
                    continue
                cols.add(c)
                diagPos.add(r+c)
                diagNeg.add(r-c)
                board[r][c] = 'Q'
                backtracking(r+1)
                board[r][c] = '.'
                diagNeg.remove(r-c)
                diagPos.remove(r+c)
                cols.remove(c)
        backtracking(0)
        return res