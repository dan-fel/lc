class node():
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sameTree(p_root, q_root):
    if not p_root and not q_root:
        return True
    
    if p_root and q_root and p_root.val == q_root.val:
        return sameTree(p_root.left, q_root.left) and sameTree (p_root.right, q_root.right)
    else:
        return False

def subTree(root, subroot):
    if not root:
        return False

    if sameTree(root, subroot):
        return True
        
    left = subTree(root.left, subroot)
    right = subTree(root.right, subroot)

    if left or right:
        return True

    return False
    
    

    

#tree = node(4, node(2, node(1), node(3)), node(7, node(6), node(13)))        
tree = node(3, node(4, node(1), node(2, node(0))), node(5))
tree2 = node(4, node(1), node(2))
#tree2 = node(4, node(2, node(1), node(3)), node(7, node(6), node(9)))        

print(subTree(tree, tree2))
#bfs(tree)



