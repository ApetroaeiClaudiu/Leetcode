class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ''
        while a and b:
            aL = int(a[-1])
            bL = int(b[-1])
            cL = aL + bL + carry
            if cL == 2:
                cL = 0
                carry = 1
            elif cL == 3:
                cL = 1
                carry = 1
            else:
                carry = 0
            result = str(cL) + result 
            a = a[:-1]
            b = b[:-1]
        
        while a:
            aL = int(a[-1])
            cL = aL + carry
            if cL == 2:
                cL = 0
                carry = 1
            else:
                carry = 0
            result = str(cL) + result 
            a = a[:-1]

        while b:
            bL = int(b[-1])
            cL = bL + carry
            if cL == 2:
                cL = 0
                carry = 1
            else:
                carry = 0
            result = str(cL) + result
            b = b[:-1]

        if carry == 1:
            result = str(carry) + result

        return result
