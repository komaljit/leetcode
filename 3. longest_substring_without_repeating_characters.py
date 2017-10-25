class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        c_s = ""
        m = 0
        for i in range (0,len(s)):
            if s[i] in c_s:
                c_s = c_s[(c_s.index(s[i])) + 1:] + s[i]
                i = i+1
            else:
                c_s = c_s+s[i]
                m = max(len(c_s),m)
                i = i+1
        return m
