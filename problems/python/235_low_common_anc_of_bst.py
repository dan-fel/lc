# Definition for a binary tree TreeNode.
class TreeNode():
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':                
        while root:        
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:                
                root = root.right
            else:                
                return root
            
tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))

tree2 = TreeNode(2, TreeNode(1))
p = TreeNode(2)
q = TreeNode(4)

sol = Solution()

print(sol.lowestCommonAncestor(tree, p, q).val)