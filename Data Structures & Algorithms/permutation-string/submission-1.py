class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0]*26
        for s in s1:
            s1_freq[ord(s)-ord('a')]+=1
        for i in range(len(s2)-len(s1)+1):
            s2_freq = [0]*26
            for j in range(len(s1)):
                s2_freq[ord(s2[i+j])-ord('a')]+=1
            if s1_freq==s2_freq:
                return True
        return False
