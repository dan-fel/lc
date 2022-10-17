class node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



'It should return the diameter of from each node, it feels doable recursively...'

def depth(root) -> int:
    if root == None:
        return 0

    left = 1 + depth(root.left)
    right = 1 + depth(root.right)

    return max(left,right)
res = 0
def diameter(root) -> int:
    global res
    if root == None:
        return 0


    left  = diameter(root.left)
    right = diameter(root.right)

    res = max(res, left + right)


    return 1 + max(left, right)



tree4 = (node(1, node(2, node(4), node(5)), node(3)))
diameter(tree4)
print(res)
