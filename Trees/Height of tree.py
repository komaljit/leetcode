from binarytree import build
root = build([1,2,3,5,6,8,9])
print(root)

def height(node):
    if node==None:
        return 0
    if not node.left and not node.right :
        return 0
    h1 = 0
    h2 = 0
    h1 = height(node.left)
    h2 = height(node.right)
    return (max(h1,h2)+1)

print(height(root))

"""
Input:
    __1__
   /     \
  2       3
 / \     / \
5   6   8   9

output: 2
"""
