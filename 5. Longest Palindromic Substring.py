class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return 0
        maxlen=1
        start=0
        for i in xrange(len(s)):
            if i-maxlen >= 1 and s[i-maxlen-1:i+1] == s[i-maxlen-1:i+1][::-1]:
                start = i-maxlen-1
                maxlen += 2 
                continue
            if i-maxlen >= 0 and s[i-maxlen:i+1] == s[i-maxlen:i+1][::-1]:
                start = i-maxlen
                maxlen += 1 
        return s[start: start+maxlen]
    
