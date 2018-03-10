var diameterOfBinaryTree = function(root) {
    var maxDiameter = -1;
    var getDepth = function(root) {
        if (root === null) {
            return 0;
        }
        var leftDepth = getDepth(root.left);
        var rightDepth = getDepth(root.right);
        
        maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);
        maxDepth = Math.max(leftDepth, rightDepth) + 1;
        return maxDepth;
    };
    
    if (root === null) return 0;
    getDepth(root);
    
    return maxDiameter;
};
