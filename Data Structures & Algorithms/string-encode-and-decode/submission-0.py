class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans+=str(len(s))+"#"+s
            # 5#Hello5#World
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        st = 0
        while st<len(s):
            ed = st
            while s[ed]!='#':
                ed+=1
            word_len = int(s[st:ed])
            st = ed+1
            word = s[st:st+word_len]
            ans.append(word)
            st += word_len
        return ans