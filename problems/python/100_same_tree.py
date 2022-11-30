class node():
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# def sameTree(p_root, q_root):

#     p_nodes = []
#     q_nodes = []

#     p_nodes.append(p_root)
#     q_nodes.append(q_root)

#     while(len(p_nodes) > 0):
#         p_node = p_nodes.pop(0)  
#         q_node = q_nodes.pop(0)
        
#         if p_node.val != q_node.val:
#             return False
    
#         if p_node.left != None and q_node.left != None:
#             p_nodes.append(p_node.left)
#             q_nodes.append(q_node.left)
                    
#         if p_node.right != None and q_node.right != None:
#             p_nodes.append(p_node.right)
#             q_nodes.append(q_node.right)        

#         if p_node.right != None and q_node.right == None:        
#             return False
            
#         if p_node.right == None and q_node.right != None:            
#             return False

#         if p_node.left != None and q_node.left == None:            
#             return False
            
#         if p_node.left == None and q_node.left != None:            
#             return False
                        
#     return True

# def bfs(root):

def sameTree(p_root, q_root):
    if not p_root and not q_root:
        return True
    
    if p_root and q_root and p_root.val == q_root.val:
        return sameTree(p_root.left, q_root.left) and sameTree (p_root.right, q_root.right)
    else:
        return False

#     nodes = []
#     nodes.append(root)

#     while(len(nodes) > 0):
#         node = nodes.pop(0)  

#         print(node.val)

#         if node.left != None:
#             nodes.append(node.left)
#         else:
#             print("null")
#         if node.right != None:
#             nodes.append(node.right)
#         else:
#             print("null")
    
# p = node(1, node(2), None)
# q = node(1, None, node(2))

tree = node(4, node(2, node(1), node(3)), node(7, node(6), node(9)))        
tree2 = node(4, node(2, node(1), node(3)), node(7, node(6), node(9)))        
print(sameTree(tree, tree2))
#bfs(tree)



