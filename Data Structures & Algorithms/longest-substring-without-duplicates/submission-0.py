class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        l = 0
        answer = 0
        for r in range(len(s)):
            while s[r] in word:
                word.remove(s[l])
                l+=1
            word.add(s[r])
            answer = max(answer, r-l+1)
        return answer