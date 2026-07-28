class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        def dfs(i):
            if i in dp: return dp[i]
            for word in wordDict:
                if s[i:i+len(word)]==word and dfs(i+len(word)):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return dfs(0)