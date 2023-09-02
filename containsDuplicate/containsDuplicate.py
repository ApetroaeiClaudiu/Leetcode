class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occurence = {}
        for i in range(0,len(nums)):
            if occurence.has_key(nums[i]):
                occurence[nums[i]].append(i)
            else:
                occurence[nums[i]] = []
                occurence[nums[i]].append(i)
            if occurence[number] >= 2:
                return True
        
        return False
