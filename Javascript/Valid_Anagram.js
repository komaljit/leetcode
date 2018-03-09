
var isAnagram = module.exports = function (s, t) {
  if (s === '' && t === '') return true;
  if (s.length !== t.length) return false;
  var hash = {};
  for (var i = 0; i < s.length; i++) {
    if (hash[s[i]] === undefined) {
      hash[s[i]] = 1;
    } else {
      hash[s[i]]++;
    }
    if (hash[t[i]] === undefined) {
      hash[t[i]] = -1;
    } else {
      hash[t[i]]--;
    }
  }
  return Object.keys(hash).filter(function (key) {
    return hash[key] !== 0;
  }).length === 0;
};
