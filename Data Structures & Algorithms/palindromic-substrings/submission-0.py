class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        def count(l, r):
            count = 0
            while 0<=l and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        for i in range(len(s)):
            answer+=count(i,i)
            answer+=count(i,i+1)
        return answer