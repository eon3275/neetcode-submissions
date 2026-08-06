class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        def dfs(l, r):
            if l+1>=r: return 0
            if dp[l][r]!=-1: return dp[l][r]
            coins = 0
            for k in range(l+1,r):
                coins = max(coins, dfs(l,k)+dfs(k,r)+nums[l]*nums[k]*nums[r])
            dp[l][r]=coins
            return coins
        return dfs(0, n-1)