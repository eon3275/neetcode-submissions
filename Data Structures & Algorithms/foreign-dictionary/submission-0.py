class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        ind = {c:0 for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:min_len]==w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]]+=1
                    break
        q = deque([c for c in ind if ind[c]==0])
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
                ind[nei]-=1
                if ind[nei]==0:
                    q.append(nei)
        if len(res)!=len(ind):
            return ""

        return "".join(res)