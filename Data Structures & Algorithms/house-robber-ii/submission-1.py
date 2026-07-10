class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(nums):
            prev1 = prev2 = 0
            for n in nums:
                temp = max(prev1+n, prev2)
                prev1 = prev2
                prev2 = temp
            return prev2
        return max(helper(nums[1:]), helper(nums[:-1]))
