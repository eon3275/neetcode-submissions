class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])
        def dfs(r, c, i):
            if i==len(word): return True
            if not(0<=r<N and 0<=c<M) or board[r][c]!=word[i]:
                return False
            board[r][c] = '#'
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c] = word[i]
            return res
        for i in range(N):
            for j in range(M):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False