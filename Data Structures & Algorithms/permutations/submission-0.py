class Solution: # dfs backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
            for n in nums:
                if n in curr:
                    continue
                curr.append(n)
                visited.add(n)
                backtrack(curr)
                visited.remove(n)
                curr.pop()
        backtrack([])
        return res