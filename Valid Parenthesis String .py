class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        L, R = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]
        for i in xrange(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in L and s[i+1] in R:
                dp[i][i+1] = True

        for j in xrange(2, n):
            for i in xrange(n - j):
                if s[i] == '*' and dp[i+1][i+j]:
                    dp[i][i+j] = True
                elif s[i] in L:
                    for k in xrange(i+1, i+j+1):
                        if (s[k] in R and (k == i+1 or dp[i+1][k-1]) and(k == i+j or dp[k+1][i+j])):                                                         
                            dp[i][i+j] = True
        return dp[0][-1]
