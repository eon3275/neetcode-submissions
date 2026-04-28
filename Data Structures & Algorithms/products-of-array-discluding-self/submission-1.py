class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1]*N
        pre = 1
        for i in range(N):
            ans[i]=pre
            pre*=nums[i]
        post = 1
        for i in range(N-1,-1,-1):
            ans[i]*=post
            post*=nums[i]
        return ans