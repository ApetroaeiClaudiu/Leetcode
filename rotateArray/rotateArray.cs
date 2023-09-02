public class Solution {
    public void Rotate(int[] nums, int k) {
        int n = nums.Length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            result[(i+k) % n] = nums[i];
        }

        for (int i = 0; i < n; i++) {
            nums[i] = result[i];
        }
    }
}
