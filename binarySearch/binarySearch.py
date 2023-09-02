class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        pos = (left + right)/2
        nover = False
        count = 0

        while count<len(nums):
            count = count+1
            if nums[pos] == target:
                return pos
            elif target < nums[pos]:
                right = pos
                pos = (left+right)/2    
            else:
                left = pos
                pos = (left+right)/2

        return -1   
