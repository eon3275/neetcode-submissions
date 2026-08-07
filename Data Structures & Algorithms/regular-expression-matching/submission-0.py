class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s), len(p)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        def dfs(i,j):
            if j==m: return i==n
            if dp[i][j]!=-1: return dp[i][j]
            match = i<n and (s[i]==p[j] or p[j]=='.')
            if j+1<m and p[j+1]=='*':
                ans = dfs(i,j+2) or (match and dfs(i+1,j))
            else:
                ans = match and dfs(i+1,j+1)
            dp[i][j] = ans
            return ans
        return dfs(0,0)