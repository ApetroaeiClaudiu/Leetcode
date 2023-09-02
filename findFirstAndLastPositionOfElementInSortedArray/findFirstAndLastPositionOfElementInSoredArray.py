class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = -1
        end = -1
        for i in range(0,len(nums)):
            if nums[i] == target:
                if start == -1:
                    start = i
                    end = i
                if i > end:
                    end = i
                    
        return [start, end]
