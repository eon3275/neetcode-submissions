class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        if len(s)<len(t): return 0
        dp = [[-1]*M for _ in range(N)]
        def dfs(i, j):
            if j==M: return 1
            if i==N: return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]!=t[j]:
                dp[i][j] = dfs(i+1,j)
            else:
                dp[i][j] = dfs(i+1,j+1)+dfs(i+1,j)
            return dp[i][j]
        return dfs(0,0)
