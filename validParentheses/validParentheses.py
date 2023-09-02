class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True
