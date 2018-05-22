
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.dp = [-2] * (amount+1)
        coins.sort()
        ans = self.get_min_coins_count(coins, amount)
        if ans[0] and ans[1] < amount+1:
            return ans[1]
        return -1
        
    def get_min_coins_count(self, coins, amount):
        if amount < 0:
            return [False, 0]
        if amount == 0:
            return [True, 0] 
        min_coins = [False, amount+1]
        for coin in coins:
            using_cur_coin_min = self.helper(coins, amount-coin)
            if using_cur_coin_min[0]:
                min_coins[0] = True
                min_coins[1] = min(min_coins[1], using_cur_coin_min[1])
        min_coins[1]= min_coins[1] + 1
        self.dp [amount] = min_coins
        return min_coins
    
    def helper(self, coins, amount):
        if amount < 0:
            return [False, 0]
        if self.dp[amount] > -2:
            return self.dp[amount]
        else:
            return self.get_min_coins_count(coins, amount)

