class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount+1):
                if dp[i]>dp[i-c]+1: dp[i] = dp[i-c]+1
        return -1 if dp[amount]==float('inf') else dp[amount]