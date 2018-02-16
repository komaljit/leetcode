class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]
        for i in range(1,n):
            a = dp[0]+dp[1]
            dp[0] = dp[1]
            dp[1] = a
        return dp[1]    
