class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        ROWS, COLS = len(board), len(board[0])
        res = []
        def dfs(r, c, node):
            if not (0<=r<ROWS and 0<=c<COLS) or board[r][c] not in node.children:
                return
            char = board[r][c]
            curr = node.children[char]
            if curr.word:
                res.append(curr.word)
                curr.word = None
            board[r][c] = '#'
            dfs(r+1,c,curr)
            dfs(r-1,c,curr)
            dfs(r,c+1,curr)
            dfs(r,c-1,curr)
            board[r][c] = char
            if not curr.children:
                del node.children[char]
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return res