class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def solve(i):
            if i in dp:
                return dp[i]
            if i>=len(nums):
                return 0
            dp[i] = max(solve(i+1), solve(i+2)+nums[i])
            return dp[i]
        return solve(0)