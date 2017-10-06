class Solution(object):
    def reverse(self, x):
        d = ""
        p = str(x)
        if p[0] == "-":
            d = d + "-"
            for i in range(0, len(p) - 1):
                d = d + str(p[len(p) - 1 - i])


        else:
            for i in range(0, len(p)):
                d = d + str(p[len(p) - 1 - i])

        if int(d) <= -2147483647 or int(d) >= 2147483647:
            return 0
        else:
            return int(d)