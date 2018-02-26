def lca(node,a,b):
    while node:
        if a < node.value and b< node.value:
            node = node.left
        elif a > node.value and b > node.value:
            node = node.right
        else:
            break
    return node.value
