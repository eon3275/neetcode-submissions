class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []
        def dfs(start):
            if start==len(s):
                res.append(stack[:])
                return
            for i in range(start, len(s)):
                sub = s[start:i+1]
                if sub==sub[::-1]:
                    stack.append(sub)
                    dfs(i+1)
                    stack.pop()
        dfs(0)
        return res