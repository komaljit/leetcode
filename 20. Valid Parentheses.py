class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        st, check = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in check:
                st.append(parenthese)
            elif len(st) == 0 or check[st.pop()] != parenthese:
                return False
        return len(st) ==0 

