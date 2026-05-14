# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            nodes = []
            for _ in range(size):
                curr = q.popleft()
                if curr:
                    nodes.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if nodes:
                res.append(nodes)
        return res