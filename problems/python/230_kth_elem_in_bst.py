from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        res = []
        def dfs(node):
            if not node:
                return
            
            l = dfs(node.left)
            res.append(node.val)
            r = dfs(node.right)

        dfs(root)        
        return res[k-1]

sol = Solution()
t = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1))), TreeNode(6))
sol.kthSmallest(t, 2)
