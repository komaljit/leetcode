var longestConsecutive = function(nums) {
    var maxLen = -Infinity;
    var hash = {};
    
    for(var i = 0; i < nums.length; i++) {
        hash[nums[i]] = 1;
    }
    
    var visited = {};
    
    for(i = 0; i < nums.length; i++) {
        var val = nums[i];
        if(visited[val]) {
            continue;
        }
        visited[val] = true;
        var len = 1;
        var preVal = val - 1;
        while(hash[preVal]) {
            len++
            visited[preVal--] = true;
        }
        var nxtVal = val + 1;
        while(hash[nxtVal]) {
            len++
            visited[nxtVal++] = true;
        }
        
        if(len > maxLen) {
            maxLen = len;
        }
    }
    
    return maxLen;
};
