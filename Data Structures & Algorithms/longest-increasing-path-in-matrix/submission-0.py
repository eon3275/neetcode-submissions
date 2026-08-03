class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        dp = [[-1]*M for _ in range(N)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r, c):
            if dp[r][c]!=-1:
                return dp[r][c]
            max_len = 1
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M and matrix[nr][nc]>matrix[r][c]:
                    max_len = max(max_len, 1+dfs(nr,nc))
            dp[r][c] = max_len
            return max_len
        ans = 0
        for r in range(N):
            for c in range(M):
                ans = max(ans, dfs(r,c))
        return ans