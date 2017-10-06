class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        for i in s:
            if i == "I":
                ans.append(1)
            elif i == "V":
                ans.append(5)
            elif i == "X":
                ans.append(10)
            elif i == "L":
                ans.append(50)
            elif i == "C":
                ans.append(100)
            elif i == "D":
                ans.append(500)
            elif i == "M":
                ans.append(1000)
        roman = ans[len(ans) - 1]
        for j in range(0, len(ans) - 1):
            if ans[j] < ans[j + 1]:
                roman = roman - ans[j]
            else:
                roman = roman + ans[j]
        return roman

