class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        occurence = {}
        for i in range(0,len(nums)):
            if occurence.has_key(nums[i]):
                occurence[nums[i]].append(i)
            else:
                occurence[nums[i]] = []
                occurence[nums[i]].append(i)
            for j in range(0,len(occurence[nums[i]]) - 1):
                val = occurence[nums[i]][j]
                val2 = occurence[nums[i]][j+1]
                if abs(val - val2) <= k:
                    return True
        
        return False
