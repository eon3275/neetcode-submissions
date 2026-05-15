class Solution: # better solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        return stack[k-1]