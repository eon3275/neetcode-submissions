class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2==1: return False #홀수 합은 분할 불가
        target//=2
        n = len(nums)
        dp = [[False]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True # target 0은 무조건 가능
        for i in range(1, n+1):
            curr = nums[i-1]
            for j in range(1, target+1):
                if j<curr: # 숫자가 목표보다 큼
                    dp[i][j] = dp[i-1][j] #이전 숫자 결과
                else:
                    # 안쓰거나 쓰고 남은 결과(j-curr)
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-curr]
        return dp[n][target]