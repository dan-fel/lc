class node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def depth(root) -> int:
    if root == None:
        return 0

    left = 1 + depth(root.left)
    right = 1 + depth(root.right)

    return max(left,right)

tree = node(4, node(2, node(1), node(3)), node(7, node(6), node(9)))        

tree2 = node(4)        

tree3 = node(4, node(2), node(3))        


print(depth(tree))
print(depth(tree2))
print(depth(tree3))