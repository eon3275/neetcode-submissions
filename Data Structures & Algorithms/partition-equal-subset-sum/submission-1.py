class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2==1: return False
        target//=2
        dp = [False]*(target+1)
        dp[0] = True
        for curr in nums:
            # 중복 연산 방지를 위한 역방향 탐색
            for j in range(target, curr-1,-1):
                # 안쓰거나 이전 결과에 반영
                dp[j] = dp[j] or dp[j-curr]
        return dp[target]