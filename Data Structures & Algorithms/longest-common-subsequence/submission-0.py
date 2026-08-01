class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)>len(text2):
            text1, text2 = text2, text1
        n, m = len(text1), len(text2)
        dp = [0]*(n+1)
        for i in range(m):
            prev = 0
            for j in range(n):
                tmp = dp[j+1]
                if text1[j]==text2[i]:
                    dp[j+1] = prev+1
                else:
                    dp[j+1] = max(dp[j], dp[j+1])
                prev = tmp
        return dp[n]