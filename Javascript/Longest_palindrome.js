var longestPalindrome = function(s) {
    var map = {};
    var number = 0;
    var hasOdd = false;

    s.split('').forEach(i => map[i] === undefined ? map[i] = 1 : map[i]++);

    for(var i in map) {
        if(map[i] % 2 === 0) {
            number += map[i];
        } else if(map[i] > 2) {
            number += map[i] - 1;
            hasOdd = true;
        } else {
            hasOdd = true;
        }
    }

    if(hasOdd) number++;

    return number;
};
