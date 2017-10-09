class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        ans =""
        a="11"
        while n > 2:
            c = 1
            for i in range (0,len(a)):
                if i+1<len(a):
                    if a[i] == a[i + 1]:
                        c = c + 1
                    else:
                        ans=ans+str(c)+a[i]
                        c=1
                elif i+1==len(a):
                    ans=ans+str(c)+a[i]
            a=ans
            ans=""
            n=n-1
        return a


