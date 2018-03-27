// Number of 1 Bits
var hammingWeight = function(n) {
    var ret = 0;
    for(var power = 32; power >= 0; power--) {
        var exponent = Math.pow(2, power);
        if (n >= exponent) {
            ret++;
            n -= exponent;
        }
    }
    return ret;
};

var hammingDistance = function(x, y) {
    return hammingWeight(x ^ y);
};
