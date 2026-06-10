class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtracking(i, curr):
            res.append(curr.copy())
            for j in range(i, len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                backtracking(j+1, curr)
                curr.pop()
        backtracking(0, [])
        return res
