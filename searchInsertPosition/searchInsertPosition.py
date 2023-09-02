class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        valid = False

        if target < nums[0]:
            return 0
        for i in range (0, len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                valid = True
            if target < nums[i] and valid == True:
                return i

        return i+1
