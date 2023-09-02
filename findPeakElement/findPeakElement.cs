public class Solution {
    public int FindPeakElement(int[] nums) {
        if (nums.Length == 1) {
            return 0;
        }
        
        for (int i = 0; i < nums.Length; i++) {
            if (i - 1 == -1) {
                if ( nums[i] > nums[i+1]) {
                    return i;
                }
            } else if (i + 1 == nums.Length) {
                if (nums[i] > nums[i-1]) {
                    return i;
                }
            } else if ( nums[i] > nums[i-1] && nums[i] > nums[i+1]) {
                return i;
            }
        }
        return -1;
    }
}
