var preorderTraversal = function(root) {
    if(root === null) return [];
    var ret = [];

    function pre(root) {
        if(root) {
            ret.push(root.val);
            pre(root.left);
            pre(root.right);
        }
    }

    pre(root);
    return ret;
};
