public class Solution {
    public int MajorityElement(int[] nums) {

        Dictionary<int, int> occurences = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            if (occurences.ContainsKey(nums[i])) {
                occurences[nums[i]] = occurences[nums[i]] + 1;
            } else {
                occurences.Add(nums[i], 1);
            }
        }
        
        foreach(KeyValuePair<int, int> entry in occurences) {
            if (entry.Value > nums.Length/2) {
                return entry.Key;
            }
        }
        return 0;
    }
}
