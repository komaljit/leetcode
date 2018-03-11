var maxProfit = function(prices) {
    var min = Number.MAX_VALUE;
    var profit = 0;
    
    for(var i = 0; i < prices.length; i++) {
        min =  Math.min(min, prices[i]);   
        profit = Math.max(profit, prices[i] - min);
    }
    
    return profit;
};
