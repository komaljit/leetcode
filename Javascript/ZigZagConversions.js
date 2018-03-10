var convert = function(s, numRows) {
    var chars = s.split('');
    var arrs = [];
    for(var k = 0; k < numRows; k++) {
        arrs.push([]);
    }

    var i = 0;
    while(i < chars.length) {
        for(var x = 0; x < numRows && i < chars.length; x++) {
            arrs[x].push(chars[i++]);
        }
        for(var x = numRows - 2; x > 0 && i < chars.length; x--) {
            arrs[x].push(chars[i++]);
        }
    }

    var ret = '';
    arrs.map(function(item) {
            ret = ret.concat(item.join(''));
            });
    return ret;
};
