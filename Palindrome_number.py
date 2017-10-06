class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        for i in range(0, len(str(x)) - 1):

            if (str(x)[i]) == (str(x)[len(str(x)) - i - 1]):
                pass
            else:
                return False

        return True



