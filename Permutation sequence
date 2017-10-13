class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = range(1, n+1)
        permut = ''
        k -= 1
        while n > 0:
            n -= 1
            ind, k = divmod(k, math.factorial(n))
            permut += str(num[ind])
            num.remove(num[ind])

        return permut
