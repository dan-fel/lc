

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            left_height = 1 + dfs(root.left)
            right_height = 1 + dfs(root.right)


            if abs(left_height - right_height) > 1:
                self.balanced = False

            return max(left_height, right_height)


        dfs(root)
        return self.balanced

tree = (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)))
sol = Solution()

print(sol.isBalanced(tree))

