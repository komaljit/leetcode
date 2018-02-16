/**
 * @param {number} n
 * @return {number}
 */

// Dp solution for climbing problem
var climbStairs = function(n) {
    
    var a = 1;
    var b = 1;
    for(i = 1;i<n;i++){
        var temp = b
        b = a + b;
        a = temp
    }
    return b
};
