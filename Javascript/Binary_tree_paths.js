var binaryTreePaths = function(root) {
    if(root === null) {
        return [];
    }
    var ret = [];
    var str = arguments[1] ? arguments[1] : '';
    if(str) {
        str = str + '->' + root.val;
    } else {
        str = root.val + '';
    }
    if(root.left === null && root.right === null)  {
        ret.push(str);
    }

    if(root.left) {
        var leftRet = binaryTreePaths(root.left, str);
        Array.prototype.push.apply(ret, leftRet);
    }
    if(root.right) {
        var rightRet = binaryTreePaths(root.right, str);
        Array.prototype.push.apply(ret, rightRet);
    }
    return ret;
};
