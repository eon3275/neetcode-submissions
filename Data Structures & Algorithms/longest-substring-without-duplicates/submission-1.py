class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = {}
        l = 0
        answer = 0
        for r in range(len(s)):
            if s[r] in word:
                l = max(l, word[s[r]]+1)
            word[s[r]] = r
            answer = max(answer, r-l+1)
        return answer