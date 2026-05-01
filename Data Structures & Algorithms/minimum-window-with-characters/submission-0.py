class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        target = {}
        for c in t:
            target[c] = target.get(c, 0)+1
        window = {}
        window_count, target_count = 0, len(target)
        answer_idx, answer_len = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0)+1
            if char in target and window[char]==target[char]:
                window_count+=1
            while window_count==target_count:
                if (r-l+1)<answer_len:
                    answer_len = r-l+1
                    answer_idx = [l, r]
                window[s[l]]-=1
                if s[l] in target and window[s[l]]<target[s[l]]:
                    window_count-=1
                l+=1
        l, r = answer_idx
        return s[l:r+1] if answer_len!=float('inf') else ""
