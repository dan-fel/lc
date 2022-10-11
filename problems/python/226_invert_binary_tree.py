from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        self.invertTree(root.right)
        self.invertTree(root.left)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root
        
def print_tree(root):
    if root == None: 
        return

    print(root.val)

    print_tree(root.right)
    print_tree(root.left)
    
        
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))

sol = Solution()

print_tree(tree)
sol.invertTree(tree)
print("---------------")
print_tree(tree)