class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, root)
        
    def helper(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if not node1.val == node2.val:
            return False
        if self.helper(node1.left, node2.right):
            return self.helper(node1.right, node2.left)
        return False
