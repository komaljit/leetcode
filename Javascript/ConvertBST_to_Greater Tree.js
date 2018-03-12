/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var convertBST = function(root) {
    var sum = 0;
    function traverse (root) {
        if (root === null) return;
        traverse(root.right);
        root.val = root.val + sum;
        sum = root.val;
        traverse(root.left);
    }

    traverse(root);
    return root;
};


/**
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
          
*/          
