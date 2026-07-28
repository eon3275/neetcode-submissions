class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1]*N
        for i in range(1,N):
            for j in range(i): # 내 앞보다 작은 수가 있으면 해당 수열 + 1의 길이
                if nums[i]>nums[j]: dp[i] = max(dp[i], dp[j]+1)
        return max(dp)