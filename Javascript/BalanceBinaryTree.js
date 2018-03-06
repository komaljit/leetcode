var maxDeepth = function(root) {
    if(root === null) {
        return 0;
    } else {
        return Math.max(maxDeepth(root.left), maxDeepth(root.right)) + 1;
    }
}
var isBalanced = function(root) {
    if(root === null) {
        return true;
    }
    var leftDeepth = maxDeepth(root.left);
    var rightDeepth = maxDeepth(root.right);

    if(Math.abs(leftDeepth - rightDeepth) <= 1
        && isBalanced(root.left)
        && isBalanced(root.right)
    ) {
        return true;
    } else {
        return false;
    }
};
