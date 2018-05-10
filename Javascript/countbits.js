var countBits = function(num) {
  var ret = [0];
  var j = 1;
  for(var i = 1; i <= num; i++) {
    if(i == 1) {ret.push(1);continue;}
    if(i == Math.pow(2, j+1)) j++;
    ret.push(ret[i - Math.pow(2, j)] + 1);
  }
  return ret;
};
