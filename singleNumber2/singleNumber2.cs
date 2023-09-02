public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> occurences = new Dictionary<int, int>();

        for (int i = 0; i< nums.Length; i++) {
            if (occurences.ContainsKey(nums[i])) {
                occurences[nums[i]] = occurences[nums[i]] + 1;
            } else {
                occurences.Add(nums[i], 1);
            }
        }
        int value = occurences.FirstOrDefault(x => x.Value == 1).Key;

        return value;
    }
}
