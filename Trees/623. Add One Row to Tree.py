def addOneRow(self, root, v, d):
    """
    :type root: TreeNode
    :type v: int
    :type d: int
    :rtype: TreeNode
    """
    if root == None:
        return root
    elif d == 1:
        node = TreeNode(v)
        node.left = root
        return node
    elif d == 2:
        node1 = TreeNode(v)
        node2= TreeNode(v)
        node1.left = root.left
        node2.right = root.right
        root.left = node1
        root.right = node2
        return root
    else:
        self.addOneRow(root.left, v, d-1)
        self.addOneRow(root.right, v, d-1)
        return root
