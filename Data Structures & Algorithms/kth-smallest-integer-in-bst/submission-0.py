class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = None
        def dfs(node):
            if not node or self.res:
                return
            dfs(node.left)
            self.cnt+=1
            if self.cnt==k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res