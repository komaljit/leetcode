class Solution(object):
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.mode = []
        self.max_count = 0
        self.cur = [0,0]
        if not root:
            return []
        self.get_mode(root)
        return self.mode
        
    def get_mode(self, root):
        if not root:
            return
        count = 1
        self.get_mode(root.left)
        if self.cur[1] == root.val:
            self.cur[0] += 1
        else:
            self.cur[1] = root.val
            self.cur[0] = 1
        if self.max_count < self.cur[0]:
            self.max_count = self.cur[0]
            self.mode = [self.cur[1]]
        elif self.max_count == self.cur[0] and self.mode[-1] != self.cur[1]:
            self.mode.append(self.cur[1])
        self.get_mode(root.right)
        
