class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        pow = 10

        for digit in digits:
            number = number*pow + digit
        
        number = number + 1
        result = []
        while number != 0:
            result.insert(0, number%10)
            number = number/10
        
        return result
