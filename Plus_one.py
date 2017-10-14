class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=0
        pow=len(digits)-1
        if digits[0]==0:
            return [1]
        else:
            for i in digits:
                num=num+(i*(10**pow))
                pow=pow-1
            num=str(num+1)
            ret=[]
            for i in num:
                ret.append(int(i))
            return ret
    
