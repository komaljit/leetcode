def insert(node, val):
    if node == None:
        return Node(val)
    if val < node.value and val > node.left.value:
        a = node.left
        node.left = Node(val)
        node.left.left = a
    elif val > node.value and val < node.left.value:
        a = node.right
        node.right = Node(val)
        node.right.right = a
    return node
